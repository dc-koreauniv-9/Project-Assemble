from flask import Flask,render_template
#from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import g
import os

app = Flask(__name__)


@app.route('/')
@app.route('/1p/')
def hello_world():
    conn = sqlite3.connect('naver_news.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("select * from table2 where id< 10")
    rows = c.fetchall()
    return render_template('1index.html', table=rows)

@app.route('/2_1p/')
def hello_world2():
    conn = sqlite3.connect('naver_news.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("select * from table2 where id< 1001")
    rows = c.fetchall()
    return render_template('2_1news.html',rows = rows)

@app.route('/2_2p/')
def hello_world3():
    conn = sqlite3.connect('TheMinJoo.db')
    conn.row_factory = sqlite3.Row
    c1 = conn.cursor()
    c1.execute("select * from table1 where id<1001")
    rows = c1.fetchall()
    return render_template('2_2TheMinJoo.html',rows = rows)

@app.route('/2_3p/')
def hello_world4():
    conn = sqlite3.connect('libertykorea0813.db')
    conn.row_factory = sqlite3.Row
    c2 = conn.cursor()
    c2.execute("select * from table1 where id<1001")
    rows = c2.fetchall()
    return render_template('2_3LibertyKorea.html',rows = rows)

@app.route('/4p/')
def hello_world5():
    return render_template('4tables.html')



if __name__ == '__main__':
    app.run()
