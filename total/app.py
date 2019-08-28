from flask import Flask,render_template, request
#from flask_sqlalchemy import SQLAlchemy
import sqlite3
import json
import pickle
from Model import tfidf_LR
from flask import g
import os

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/1p/', methods=['POST', 'GET'])
def hello_world():
    conn = sqlite3.connect('naver_news.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("select * from db20190828 where id< 100")
    rows = c.fetchall()
    if request.method == 'POST':
        print(request.data)
        idx = int(request.data.decode("utf-8").split('=')[1])
        classifier = tfidf_LR()
        prob_article = list(classifier.predict_article(rows[idx]["content"])[0])
        most_polarized = list(classifier.predict_sentences(rows[idx]["content"]))
        print(prob_article)
        print(most_polarized)
        return json.dumps({'predicted': prob_article, 'most_polarized':most_polarized})

    return render_template('1index.html', table=rows)

@app.route('/2_1p/')
def hello_world2():
    conn = sqlite3.connect('naver_news.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("select * from db20190828 where id< 101")
    rows = c.fetchall()
    return render_template('2_1news.html',rows = rows)

@app.route('/2_2p/')
def hello_world3():
    conn = sqlite3.connect('TheMinJoo.db')
    conn.row_factory = sqlite3.Row
    c1 = conn.cursor()
    c1.execute("select * from table1 where id<101")
    rows = c1.fetchall()
    return render_template('2_2TheMinJoo.html',rows = rows)

@app.route('/2_3p/')
def hello_world4():
    conn = sqlite3.connect('libertykorea0813.db')
    conn.row_factory = sqlite3.Row
    c2 = conn.cursor()
    c2.execute("select * from table1 where id<101")
    rows = c2.fetchall()
    return render_template('2_3LibertyKorea.html',rows = rows)

@app.route('/4p/', methods=['POST', 'GET'])
def hello_world5():
    if request.method == 'POST':
        text = request.data.decode('utf-8')
        classifier = tfidf_LR()
        prob_text = list(classifier.predict_article(text)[0])
        most_polarized = list(classifier.predict_sentences(text))
        print(prob_text, most_polarized)
        return json.dumps({'predicted': prob_text, 'most_polarized': most_polarized})

    return render_template('4tables.html')

if __name__ == '__main__':
    app.run()

