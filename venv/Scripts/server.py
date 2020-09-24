from flask import Flask, render_template
from flask_cors import CORS, cross_origin   
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return render_template('player_viewer.html')
    