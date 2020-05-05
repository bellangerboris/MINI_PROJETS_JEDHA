from flask import Flask,render_template,url_for,request
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method=='POST':
        cv_Vocabulary = open('cv_Vocabulary.pkl','rb')
        vocabulary = joblib.load(cv_Vocabulary)
        NB_spam_model = open('NB_spam_model.pkl','rb')
        clf = joblib.load(NB_spam_model)
        message = request.form['message']
        data = [message]
        cv=CountVectorizer(vocabulary=vocabulary)
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)
