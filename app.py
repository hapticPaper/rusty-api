from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/welcome')
def welcome():
    return render_template('index.html', name='ian')


@app.route('/')
def index():
    return {'dataSetResults':[1,2,3,4,5,6,7,8,9,10]}

if __name__ =='__main__':
    app.run(threaded=True, host='0.0.0.0', port=80)