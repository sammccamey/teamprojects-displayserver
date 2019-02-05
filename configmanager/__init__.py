import io
import flask
from flask import Flask, jsonify, request, send_file

app = Flask(__name__)

@app.route('/')
def root():
    return 'WAKEUPINATOR 3000 Config Server'

@app.route('/get')
def getcfg():
    return ''
