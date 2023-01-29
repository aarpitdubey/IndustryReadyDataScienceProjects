from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    return "Docker-Project : Hello World"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)