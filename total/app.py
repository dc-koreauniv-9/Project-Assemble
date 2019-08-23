from flask import Flask,render_template
from models import Table1
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
    SQLACHEMY_DATABASE_URI = 'sqlite:///TheMinJoo.db',
    SQLAlCHEMY_TRACK_MODIFICATIONS = False
)

admin = Admin(app, name="anchovy")
db = SQLAlchemy(app)
admin.add_view(ModelView(Table1, db.session))

class MyModelView(ModelView):
    can_delete = False

admin.add_view(MyModelView(Table1, db.session))

@app.route('/')
@app.route('/1p/')
def hello_world():
    user = Table1.query.all()
    return render_template('1index.html',user=user)

@app.route('/2p/')
def hello_world2():
    return render_template('2introduce.html')

@app.route('/3p/')
def hello_world3():
    return render_template('3charts.html')

@app.route('/4p/')
def hello_world4():
    return render_template('4tables.html')

# 문근영만 검색해서 뿌려줌.
# @app.route('/')
# def data_filter():
#     user = User.query.filter_by(username='문근영')
#     return render_template('index.html', user=user)

if __name__ == '__main__':
    app.run()
