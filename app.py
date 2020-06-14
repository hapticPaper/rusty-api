from flask import Flask, jsonify, render_template, send_from_directory, request
from flask_restful import reqparse
from flask_cors import CORS
import os
import random
import re, json
import math

app = Flask(__name__)
CORS(app)



@app.route('/')
def index():
    return render_template('/dashboard.html')


@app.route('/datasets')
def datasets():
    return {'datasets':['linear','linear100','base2', 'random', 'fib', 'x4', 'custom']} 


@app.route('/charts')
def charts():
    return {'charts':['bar','line','doughnut', 'radar', 'polarArea']}   

"""
THIS NEXT ROUTE SHOULDNT BE HERE
ITS ANTITHETICAL TO THE REQUIREMENTS
"""
@app.route('/welcome')
def welcome():
    name = request.args.get('name', '!')
    return render_template('/welcome.html', name=name)


def getLength():
    length = request.args.get('length', None)
    if length:
        return min(int(length), 1000)
    else:
        return 10

@app.route('/linear')
def data1():
    length = getLength()
    return {'dataSetResults':[i for i in range(1, length+1)]}

@app.route('/custom', methods=['POST', 'GET'])
def custom():
    pattern = "[0-9]x|\)x|x\(|[0-9]m|[a-z]x"
    functions = ['sqrt', 'sin', 'cos', 'tan', 'pi', 'log', 'log10']
    if request.method=='GET':
        return {'error':"This endpoint only accepts post requests with a 'formula' parameter. For example 'formula=2x'"}
    else:
        if len(request.data)>0:
            formula =  str(json.loads(request.data).get('formula', ''))
        else: 
            formula='1/x'
        
        for function in functions:
            formula = formula.replace(function, f"math.{function}")
        while len(re.findall(pattern, formula))>0:
            multipliers = re.findall(pattern, formula)
            for multiplier in multipliers:
                formula = formula.replace(multiplier, f"{multiplier[0]}*{multiplier[1]}")
        length=getLength()
        try:
            return {'dataSetResults':[eval(formula) for x in range(1, length+1)], 'formula':formula}
        except Exception as e:
            return {'error': str(e), "dataSetResults":[]}
        
    return {'dataSetResults':[eval(formula) for x in range(1, length+1)]}


@app.route('/x4')
def x4():
    length = getLength()
    return {'dataSetResults':[ 4*i for i in range(1, length+1)]}


@app.route('/linear100')
def data2():
    length = getLength()
    return {'dataSetResults':[100*i for i in range(1, length+1)]}

@app.route('/base2')
def data3():
    length = getLength()
    return {'dataSetResults':[2 ** i for i in range(1, length+1)]}

@app.route('/random')
def randomSet():
    length = getLength()
    return {'dataSetResults':[random.randint(1,100) for i in range(1, length+1)]}

@app.route('/fib')
def fib():
    length = getLength()
    a = b = 1
    fset = [a, b]
    for i in range(1, length-1):
        a, b = a + b, a
        fset.append(a)
    return {'dataSetResults':fset[:length]}

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ =='__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=os.environ['PORT'])