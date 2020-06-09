from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/welcome/<name>')
def welcome(name):
    return render_template('/welcome.html', name=name)


@app.route('/')
def index():
    return {'dataSetResults':[1,2,3,4,5,6,7,8,9,10]}

if __name__ =='__main__':
    app.run(threaded=True, host='0.0.0.0', port=os.environ['PORT'])