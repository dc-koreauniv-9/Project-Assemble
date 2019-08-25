from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///naver_news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
@app.route('/1p/')
def hello_world():
    table = Table2.query.limit(9).all()
    return render_template('1index.html', table=table)

@app.route('/2_1p/')
def hello_world2():
    return render_template('2_1news.html')

@app.route('/2_2p/')
def hello_world3():
    return render_template('2_2TheMinJoo.html')

@app.route('/2_3p/')
def hello_world4():
    return render_template('2_3LibertyKorea.html')

@app.route('/4p/')
def hello_world5():
    return render_template('4tables.html')

class Table2(db.Model):
    __tablename__ = 'table2'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)




if __name__ == '__main__':
    app.run()
