from flask import Flask, request, render_template
from flask_cors import CORS
import pandas as pd
import joblib
import json
import time
import datetime
from datetime import timedelta
import statsmodels.api as sm
import scipy.stats as stats
# from train import train

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict')
def predict():
    with open('preds.json', 'r') as f:
        file = f.read()
    return file


if __name__ == "__main__":
    app.run(port=12345, debug=True)
