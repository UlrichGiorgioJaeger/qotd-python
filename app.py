import flask
from flask import request, jsonify
import random
import socket
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

quotes = [
    {'id': 0,
     'quotation': 'It is not only what you do, but also the attitude you bring to it, that makes you a success.',
     'author': 'Don Schenck',
     'hostname': '{hostname}'},
    {'id': 1,
     'quotation': 'Knowledge is power.',
     'author': 'Francis Bacon',
     'hostname': '{hostname}'},
    {'id': 2,
     'quotation': 'Life is really simple, but we insist on making it complicated.',
     'author': 'Confucius',
     'hostname': '{hostname}'},
    {'id': 3,
     'quotation': 'This above all, to thine own self be true.',
     'author': 'William Shakespeare',
     'hostname': '{hostname}'},
    {'id': 4,
     'quotation': 'I got a fever, and the only prescription is more cowbell.',
     'author': 'Will Ferrell',
     'hostname': '{hostname}'},
    {'id': 5,
     'quotation': 'Anyone who has ever made anything of importance was disciplined.',
     'author': 'Andrew Hendrixson',
     'hostname': '{hostname}'},
]

@app.route('/', methods=['GET'])
def home():
    return prepareResponse("qotd")

@app.route('/version', methods=['GET'])
def version():
    return prepareResponse("3.0.0")

@app.route('/writtenin', methods=['GET'])
def writtenin():
    return prepareResponse("Python")

@app.route('/quotes', methods=['GET'])
def getQuotes():
    return prepareResponse(jsonify(replaceHostname(quotes)))

@app.route('/quotes/<int:id>', methods=['GET'])
def getQuoteById(id):
    return prepareResponse(jsonify(replaceHostname(quotes[id])))

@app.route('/quotes/random', methods=['GET'])
def getRandom():
    n = random.randint(0,5)
    return prepareResponse(jsonify(replaceHostname(quotes[n])))

def prepareResponse(response):
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def replaceHostname(jsondoc):
    q = json.dumps(jsondoc)
    q = q.replace('{hostname}', socket.gethostname())
    return json.loads(q)

if __name__ == '__main__':
    app.run(host="localhost", port=10000)