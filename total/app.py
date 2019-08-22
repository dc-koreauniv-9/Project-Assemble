from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
@app.route('/1p/')
def hello_world():
    return render_template('index1p.html')

@app.route('/2p')
def model():
    return render_template('index2p.html')

@app.route('/3p/')
def hello_world3():
    return render_template('index3p.html')

@app.route('/4p/')
def hello_world4():
    return render_template('index4p.html')


if __name__ == '__main__':
    app.run()
