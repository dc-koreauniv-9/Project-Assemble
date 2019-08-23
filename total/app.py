from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
@app.route('/1p/')
def hello_world():
    return render_template('1index.html')

@app.route('/2p/')
def hello_world2():
    return render_template('2introduce.html')

@app.route('/3p/')
def hello_world3():
    return render_template('3charts.html')

@app.route('/4p/')
def hello_world4():
    return render_template('4tables.html')



if __name__ == '__main__':
    app.run()
