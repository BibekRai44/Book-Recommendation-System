from flask import Flask,render_template,request,jsonify
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
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['Book-Rating'].values),
                           rating=list(popular_df['avg-book-rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/list')
def search_list():
    return render_template('list.html')

@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)

    return render_template('recommend.html',data=data)
if __name__ == '__main__':
    app.run(debug=True)