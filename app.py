from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd

popular_df = pd.compat.pickle_compat.load(open('model/popular_df.pkl','rb'))
pt = pd.compat.pickle_compat.load(open('model/pt.pkl','rb'))
books = pd.compat.pickle_compat.load(open('model/books.pkl','rb'))
similarity_scores = pd.compat.pickle_compat.load(open('model/similarity_scores.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)