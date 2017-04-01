from flask import Flask, render_template
from flask import request
from flask import jsonify
from flask import json

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

@app.route("/keyboard")
def keyboard():
    return jsonify(type="text")
    # return jsonify(type="buttons", buttons=["Test1", "Test2"])

@app.route("/message", methods=['POST'])
def message():
    data = request.data.decode('utf-8', 'replace')
    query = json.loads(request.data)
    print("USER >> " + query["content"])

    response = chatbot.get_replay(query["content"])
    print("Chat >> " + str(response))
    text = {
        "message": {
            "text": str(response)
        }
    }
    return jsonify(text)


if __name__ == "__main__":
    app.run()
    #app.run(host='0.0.0.0', port='5000')