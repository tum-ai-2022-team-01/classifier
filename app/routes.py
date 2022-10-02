from app import app
from flask import request

from models.main import classifier

@app.route('/')
def handler():
  text = request.args.get('text', default = '', type = str)
  return classifier(text)
