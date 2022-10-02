
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

from models.classifiers import BERTClassifier
from models.resources import low_risk_generic_answer, high_risk_dict, prohibited_dict

NUM_RISK_CLASSES = 3
NUM_PROHIBITED_CASES = 4
NUM_HIGH_RISK_CASES = 5
RISK_CLASSIFIER_CHECKPOINT = 'models/checkpoints/risk_classifier.pt'
HIGH_RISK_CASE_CLASSIFIER_CHECKPOINT = 'models/checkpoints/high_risk_case_classifier.pt'
PROHIBITED_CASE_CLASSIFIER_CHECKPOINT = 'models/checkpoints/prohibited_case_classifier.pt'
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Instantiate all models
risk_classifier = BERTClassifier(NUM_RISK_CLASSES)
high_risk_case_classifier = BERTClassifier(NUM_HIGH_RISK_CASES)
prohibited_case_classifier = BERTClassifier(NUM_PROHIBITED_CASES)

# Load all model checkpoints
risk_classifier.load_state_dict(torch.load(RISK_CLASSIFIER_CHECKPOINT))
high_risk_case_classifier.load_state_dict(
    torch.load(HIGH_RISK_CASE_CLASSIFIER_CHECKPOINT))

# Prohibited case classifier not properly trained yet!
#  
# prohibited_case_classifier.load_state_dict(
#     torch.load(PROHIBITED_CASE_CLASSIFIER_CHECKPOINT))


def classify_user_input(text):
  classes = ['High-risk', 'Low-risk', 'Prohibited']
  tokens = tokenizer.encode_plus(text, return_tensors="pt")
  logits = risk_classifier(**tokens).detach().numpy()
  prediction = classes[np.argmax(logits)]
  return prediction


def classify_high_risk(text):
  tokens = tokenizer.encode_plus(text, return_tensors="pt")
  logits = high_risk_case_classifier(**tokens).detach().numpy()
  prediction = np.argmax(logits)
  return prediction + 1 # start counting from 1


def classify_prohibited(text):
  tokens = tokenizer.encode_plus(text, return_tensors="pt")
  logits = prohibited_case_classifier(**tokens).detach().numpy()
  prediction = np.argmax(logits)
  return prediction + 1  # start counting from 1


def classifier(text):
  risk_class = classify_user_input(text)
  risk = ""
  description = ""
  if risk_class == 'Low-risk':
    risk = 'low'
    description = low_risk_generic_answer
  elif risk_class == 'High-risk':
    risk = 'medium'
    annex_num = classify_high_risk(text)
    description = """
    The described AI use case might be classified as high-risk under the EU AI Act. Please seek further legal advice.

    Why is it classified as high-risk?

    """ + high_risk_dict[annex_num]
  else:
    risk = 'high'
    explanation_num = classify_prohibited(text)
    description = """
    The described AI use case is likely to be prohibited in the European Union. Please seek further legal advice.

    Why is the use case prohibited?
    The use case involves one or more of these factors:
    """ + prohibited_dict[explanation_num]

  response = {
      'risk': risk,
      'title': "{} AI use".format(risk_class),
      'description': description
  }

  return response