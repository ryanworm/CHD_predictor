import flask 
from flask import request, render_template, jsonify
#from predictor_api import make_predictions

app = flask.Flask(__name__)

# @app.route("/page_name", methods = ["GET","POST"])
# def do_something():
#     flask.render_template('page_name.html',var_1 = v1, var_2 = v2

# return flask.render_template('predictor.html',
#                               chat_in=x_input,
#                               prediction=predictions)

@app.route("/")
def main():
    return render_template('health_intake.html')

@app.route("/request", methods= ['POST'])
def result():
    if request.method == 'POST':
        age = request.form.get('age')
        sex = request.form.get('male') 
        sysBP = request.form.get('sysBP')
        chol = request.form.get('totChol')
        glucose = request.form.get('glucose')
        bmi = request.form.get('BMI')
        restingHR = request.form.get('heartRate')
        cigs = request.form.get('cigsPerDay')
        education = request.form.get('education')
        bpMed = request.form.get('BPMeds')
        stroke = request.form.get('prevalentStroke')

        form_data = age, sex, sysBP, chol, glucose, bmi, restingHR, cigs, education, bpMed, stroke

    #return results(data=form_data)
    #process data

    #model.load('modle.h5')

    #predictions= model.predict(data)

    return jsonify(form_data) #render_template('results.html', results = predictions)

if __name__=="__main__":
    app.run(debug=True)