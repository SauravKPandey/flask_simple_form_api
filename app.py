from flask import Flask, render_template, request, redirect, url_for, jsonify
import numpy as np


## Create a simple flask application

app=Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to the new web Flask app</h1>"

@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"

##Variable rule
@app.route("/success/<int:score>")
def success_can(score):
    return "The person has passed and the score is: "+ str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "Student Failed, score is: "+ str(score)
@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method =="GET":
        return render_template('form.html')
    else:
        maths= float(request.form['Maths'])
        science = float(request.form['Science'])
        english= float(request.form['English'])

        average= np.average([maths,science,english])
        res=''
        if average>50:
            res='success_can'
        else:
            res='false'
        
        return redirect(url_for(res, score=average ))

        #return render_template('form.html', score= average)
@app.route('/api', methods=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val= float(dict(data)['a'])
    b_val= float(dict(data)['b'])

    return jsonify(a_val+b_val)

if __name__ == "__main__":
    app.run(debug=True)