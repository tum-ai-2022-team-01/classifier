from app import app
from flask import request

def classifier(text):
  return {
    'risk': 'prohibited',
    'explanation': 'A AI-controlled world domination system (Terminator) is probably a bad idea...'
  }

@app.route('/')
def handler():
  text = request.args.get('text', default = '', type = str)
  return classifier(text)
