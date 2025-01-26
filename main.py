from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data
with open('data.json') as f:
    data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref')
    if pref:
        for student in data:
            if student['pref'] == pref:
                result.append(student)
        return jsonify(result)
    return jsonify(data)

@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student['id'] == id:
            return jsonify(student)

@app.route('/stats')
def get_stats():
  
    chicken = 0
    compSciM = 0
    compSciS = 0
    fish = 0
    infoTechM = 0
    infoTechS = 0
    vegetable = 0
  
    for student in data:
        if(student['pref'] == "Chicken"):
            chicken+=1
        if(student['pref'] == "Fish"):
            fish+=1
        if(student['pref'] == "Vegetable"):
            vegetable+=1
        if(student['programme'] == "Computer Science (Major)"):
            compSciM+=1
        if(student['programme'] == "Computer Science (Special)"):
            compSciS+=1
        if(student['programme'] == "Information Technology (Major)"):
            infoTechM+=1
        if(student['programme'] == "Information Technology (Special)"):
            infoTechS+=1

    result = {
        "Chicken": chicken,
        "Computer Science (Major)": compSciM,
        "Computer Science (Special)": compSciS,
        "Fish": fish,
        "Information Technology (Major)": infoTechM,
        "Information Technology (Special)": infoTechS,
        "Vegetable": vegetable
    }
    return jsonify(result)

@app.route('/add/<a>/<b>')
def add(a, b):
    return str(int(a) + int(b))

@app.route('/subtract/<a>/<b>')
def subtract(a, b):
    return str(int(a) - int(b))

@app.route('/multiply/<a>/<b>')
def multiply(a, b):
    return str(int(a) * int(b))

@app.route('/divide/<a>/<b>')
def divide(a, b):
    return str(int(a) / int(b))

app.run(host='0.0.0.0', port=8080, debug=True)
