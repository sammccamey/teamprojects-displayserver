import io
import configdata
import flask
from flask import Flask, jsonify, request

configdata.setup()
app = Flask(__name__)

@app.route('/')
def root():
    return 'WAKEUPINATOR 3000 Config Server'

@app.route('/get')
def getcfg():
    return jsonify(configdata.retrieve())

@app.route('/choices')
def getchoices():
    return jsonify(configdata.possibilities)

@app.route('/set', methods=['POST'])
def setcfg():
    configdata.save(request.json)
    return jsonify(configdata.retrieve())
