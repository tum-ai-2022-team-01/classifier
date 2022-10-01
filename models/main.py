
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

from classifier.models.Classifiers import BERTClassifier

NUM_RISK_CLASSES = 3
NUM_PROHIBITED_CASES = 4
NUM_HIGH_RISK_CASES = 4
RISK_CLASSIFIER_CHECKPOINT = 'checkpoints/risk_classifier.pt'
HIGH_RISK_CASE_CLASSIFIER_CHECKPOINT = 'checkpoints/high_risk_case_classifier.pt'
PROHIBITED_CASE_CLASSIFIER_CHECKPOINT = 'checkpoints/prohibited_case_classifier.pt'
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Instantiate all models
risk_classifier = BERTClassifier(NUM_RISK_CLASSES)
high_risk_case_classifier = BERTClassifier(NUM_HIGH_RISK_CASES)
prohibited_case_classifier = BERTClassifier(NUM_PROHIBITED_CASES)

# Load all model checkpoints
risk_classifier.load_state_dict(torch.load(RISK_CLASSIFIER_CHECKPOINT))
high_risk_case_classifier.load_state_dict(
    torch.load(HIGH_RISK_CASE_CLASSIFIER_CHECKPOINT))
prohibited_case_classifier.load_state_dict(
    torch.load(PROHIBITED_CASE_CLASSIFIER_CHECKPOINT))


def classify_user_input(text):
  classes = ['High-risk', 'Low-risk', 'Prohibited']
  tokens = tokenizer.encode_plus(text, return_tensors="pt")
  logits = risk_classifier(**tokens)
  prediction = classes[np.argmax(logits)]
  return prediction


def classify_high_risk(text):
  pass


def classify_prohibited(text):
  pass


def main(text):
  # TODO: include Annex III cases and Prohibited cases
  risk_class = classify_user_input(text)
  explanation = ""
  if risk_class == 'Low-risk':
    explanation = """TODO: Some generic answer"""
  elif risk_class == 'High-risk':
    annex_num = classify_high_risk(text)
    explanation = annex[annex_num]
  else:
    explanation_num = classify_prohibited(text)
    explanation = prohibited_cases[explanation_num]

  response = {
      'risk_category': risk_class,
      'explanation': explanation
  }

  return response