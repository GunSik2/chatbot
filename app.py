from flask import Flask, render_template

import tensorflow as tf
import random
import math
import os

from config import FLAGS
from model import Seq2Seq
from dialog import Dialog
from chatbot import ChatBot


app = Flask(__name__)

chatbot = ChatBot(FLAGS.voc_path, FLAGS.train_dir)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
    print('query', query.strip())
    response = chatbot.get_replay(query.strip())
    print('response', response)
    return str(response)

if __name__ == "__main__":
    app.run()
