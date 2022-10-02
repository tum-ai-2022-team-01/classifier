from app import app
from flask import request

from models import main

@app.route('/')
def handler():
  text = request.args.get('text', default = '', type = str)
  return main(text)
