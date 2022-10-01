import numpy as np
import pandas as pd
from sklearn import metrics
import transformers
import torch
from torch.utils.data import Dataset, DataLoader, RandomSampler, SequentialSampler
from transformers import BertTokenizer, BertModel, BertConfig

from torch import cuda
torch.cuda.empty_cache()
device = 'cuda' if cuda.is_available() else 'cpu'

RANDOM_STATE = 42
MAX_LEN = 200
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 1
LEARNING_RATE = 1e-05
NUM_RISK_CLASSES = 3
NUM_PROHIBITED_CASES = 4
NUM_HIGH_RISK_CASES = 4
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


class CustomDataset(Dataset):

    def __init__(self, dataframe, tokenizer, max_len):
        self.tokenizer = tokenizer
        self.data = dataframe
        self.text = self.data.iloc[:, 0]
        self.targets = self.data.iloc[:, 1]
        self.max_len = max_len

    def __len__(self):
        return len(self.text)

    def __getitem__(self, index):
        text = str(self.text[index])
        text = " ".join(text.split())

        inputs = self.tokenizer.encode_plus(
            text,
            None,
            add_special_tokens=True,
            max_length=self.max_len,
            pad_to_max_length=True,
            return_token_type_ids=True
        )
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        token_type_ids = inputs["token_type_ids"]

        return {
            'input_ids': torch.tensor(input_ids, dtype=torch.long),
            'attention_mask': torch.tensor(attention_mask, dtype=torch.long),
            'token_type_ids': torch.tensor(token_type_ids, dtype=torch.long),
            'targets': torch.tensor(self.targets[index], dtype=torch.float)
        }


def construct_dataloaders(dataframe, train_size=0.8, random_state=RANDOM_STATE, train_batch_size=TRAIN_BATCH_SIZE, valid_batch_size=VALID_BATCH_SIZE):
    train_dataset = dataframe.sample(
        frac=train_size, random_state=random_state)
    test_dataset = dataframe.drop(train_dataset.index).reset_index(drop=True)
    train_dataset = train_dataset.reset_index(drop=True)

    print("FULL Dataset: {}".format(dataframe.shape))
    print("TRAIN Dataset: {}".format(train_dataset.shape))
    print("TEST Dataset: {}".format(test_dataset.shape))

    train_set = CustomDataset(train_dataset, tokenizer, MAX_LEN)
    test_set = CustomDataset(test_dataset, tokenizer, MAX_LEN)

    train_params = {'batch_size': train_batch_size,
                    'shuffle': True,
                    'num_workers': 1
                    }

    test_params = {'batch_size': valid_batch_size,
                   'shuffle': True,
                   'num_workers': 1
                   }

    train_loader = DataLoader(train_set, **train_params)
    test_loader = DataLoader(test_set, **test_params)

    return train_loader, test_loader


class BERTClassifier(torch.nn.Module):
    def __init__(self, output_size):
        super(BERTClassifier, self).__init__()
        self.Bert = BertModel.from_pretrained('bert-base-uncased')
        self.final_classifier = torch.nn.Linear(768, output_size)

    def forward(self, input_ids, attention_mask, token_type_ids):
        _, output_1 = self.Bert(input_ids, attention_mask,
                                token_type_ids=token_type_ids, return_dict=False)
        output = self.final_classifier(output_1)
        return output


def loss_fn(outputs, targets):
    return torch.nn.BCEWithLogitsLoss()(outputs, targets)


def train(model, optimizer, train_loader, epoch):
    model.train()
    for _, data in enumerate(train_loader, 0):
        input_ids = data['input_ids'].to(device, dtype=torch.long)
        attention_mask = data['attention_mask'].to(device, dtype=torch.long)
        token_type_ids = data['token_type_ids'].to(device, dtype=torch.long)
        targets = data['targets'].to(device, dtype=torch.float)

        outputs = model(input_ids, attention_mask, token_type_ids)

        optimizer.zero_grad()
        loss = loss_fn(outputs, targets)
        if _ % 5000 == 0:
            print(f'Epoch: {epoch}, Loss:  {loss.item()}')

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


def validation(model, test_loader, epoch):
    model.eval()
    fin_targets = []
    fin_outputs = []
    with torch.no_grad():
        for _, data in enumerate(test_loader, 0):
            input_ids = data['input_ids'].to(device, dtype=torch.long)
            attention_mask = data['attention_mask'].to(
                device, dtype=torch.long)
            token_type_ids = data['token_type_ids'].to(
                device, dtype=torch.long)
            targets = data['targets'].to(device, dtype=torch.float)
            outputs = model(input_ids, attention_mask, token_type_ids)
            fin_targets.extend(targets.cpu().detach().numpy().tolist())
            fin_outputs.extend(torch.sigmoid(
                outputs).cpu().detach().numpy().tolist())
    return fin_outputs, fin_targets