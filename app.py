from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import base64
import sys
import os

sys.path.append(os.path.abspath('./model'))

from load import *

from utils import convert_image

import json

with open('data/mapping.json', 'r') as mapping:
    CLASS_MAPPING = json.load(mapping)

#init flask app
app = Flask(__name__)

global model, graph
model, graph = init()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict/',methods=['GET','POST'])
def predict():
    img_data = request.get_data()
    convert_image(img_data)
    X = imread('output.png',mode='L')
    X = np.invert(X)
    X = imresize(X,(28,28))
    X = X.reshape(1,28,28,1)

    with graph.as_default():
        out = model.predict(X)
        response = np.array_str(np.argmax(out))
        return str(CLASS_MAPPING[response])





if __name__ == '__main__':

    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)
