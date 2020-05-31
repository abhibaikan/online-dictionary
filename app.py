# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:34:49 2020

@author: ab
"""

from flask import Flask, request, render_template, json

app = Flask(__name__)

data = json.load(open('dictionary_data_code\\data.json'))

@app.route('/',methods=['GET','POST'])
def home():
    
    if request.method == 'POST':
        word = request.form['word']
        word = word.lower()
        if word in data:
            str1 = data[word]
            st = ''.join(str1)
            return st 
        else:
            return "word not found"
        
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
         