import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string 

df = pd.read_csv("data.csv")

#Tokenization (a list of tokens), will be used as the analyzer
#1.Punctuations are [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]
#2.Stop words in natural language processing, are useless words (data).
def process_text(text):
    
    #1 Remove Punctuationa
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    #2 Remove Stop Words
    clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('portuguese')]
    
    #3 Return a list of clean words
    return clean_words

df['message'].head().apply(process_text)



from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(analyzer=process_text)
messages_bow = vect.fit_transform(df['message'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(messages_bow, df['prediction'], test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

#Predict
newData = ["vai prejudicar teus rins tomar na AIDS"]
newX = vect.transform(newData)
y_pred = classifier.predict(newX)

print(y_pred);
