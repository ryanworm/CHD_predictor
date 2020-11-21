import flask 
from flask import request, render_template, jsonify
# from model_api import 
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
        age = int(request.form.get('age'))
        sex = request.form.get('male') 
        if sex == "Male":
            sex = 1
        else: 
            sex = 0
        sysBP = float(request.form.get('sysBP'))
        chol = float(request.form.get('totChol'))
        glucose = float(request.form.get('glucose'))
        bmi = float(request.form.get('BMI'))
        restingHR = float(request.form.get('heartRate'))
        cigs = float(request.form.get('cigsPerDay'))
        education = request.form.get('education')
        if education == "Some High School":
            education = 1
        elif education == "High School Diploma" 
            education = 2
        elif education == "College Diploma" 
            education = 3
        else:
            education = 4
        bpMed = request.form.get('BPMeds')
        if bpMed == "Yes":
            bpMed = 1
        else: 
            bpMed = 0
        stroke = request.form.get('prevalentStroke')
        if stroke == "Yes":
            stroke = 1
        else: 
            stroke = 0
        form_data = []
        form_data.append()
        age, sex, sysBP, chol, glucose, bmi, restingHR, cigs, education, bpMed, stroke

        predict_outcome = make_predictions(form_data)
        # create function under model_api
        #function predict_output:
                # take the data from form_data as single argument
                # spits out predictive results 1 or 0 (10yearCHD)
                # return prediction (0 or 1)
                # invoke predict_outcome

    #return results(data=form_data)
    #process data

    #model.load('modle.h5')

    #predictions= model.predict(data)

    return jsonify(form_data) #render_template('results.html', results = predictions)

if __name__=="__main__":
    app.run(debug=True)