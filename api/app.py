from flask import Flask, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os

app = Flask(os.path.join('api', __name__))
CORS(app)


@app.route('/')
def index():
    return render_template('/dashboard.html')

@app.route('/welcome/<name>')
def welcome(name):
    return render_template(os.path.join(app.root_path, 'api', 'templates','welcome.html'), name=name)


@app.route('/data1')
def data1():
    return {'dataSetResults':[1,2,3,4,5,6,7,8,9,10]}

@app.route('/data2')
def data2():
    return {'dataSetResults':[100*i for i in [1,2,3,4,5,6,7,8,9,10]]}

@app.route('/data3')
def data3():
    return {'dataSetResults':{i:2 ** i for i in [1,2,3,4,5,6,7,8,9,10]}}


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'api', 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ =='__main__':
    app.run(threaded=True, host='0.0.0.0', port=os.environ['PORT'])