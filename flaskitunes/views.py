from flask import Flask,render_template
# from itunes import get_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('itunes.html')