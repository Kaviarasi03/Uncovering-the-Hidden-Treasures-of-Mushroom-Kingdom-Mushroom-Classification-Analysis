import numpy as np
import os
from flask import Flask, request, render, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.application.xception import preprocess_input

model=load_model(r"mushroom.h5")
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')
@app.route('/home')
def home():
    return render_template("index.html")
@app.route('/input')
def input1():
    return render_template("input.html")
