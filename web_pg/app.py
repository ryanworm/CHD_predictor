import flask 
from flask import request, render_template, jsonify
import numpy as np
from predictor_api import predict_outcome

# from model_api import 
# from predictor_api import predict_outcome

app = flask.Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/health_intake", methods= ['POST'])
def result():
    if request.method == 'POST':
        age = int(request.form.get('age'))
        sex = request.form.get('male') 
        sex_raw = sex
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
        education_raw = education
        if education == "Some High School":
            education = 1
        elif education == "High School Diploma": 
            education = 2
        elif education == "College Diploma":
            education = 3
        else:
            education = 4
        bpMed = request.form.get('BPMeds')
        bpMed_raw = bpMed
        if bpMed == "Yes":
            bpMed = 1
        else: 
            bpMed = 0
        stroke = request.form.get('prevalentStroke')
        stroke_raw = stroke
        if stroke == "Yes":
            stroke = 1
        else: 
            stroke = 0

               
        form_data = []
        form_data.append((age, sex, sysBP, chol, glucose, bmi, restingHR, cigs, education, bpMed, stroke))
        form_data = form_data[0]        
        
        # print(form_data)

  # invoke predict_outcome
        # CHD_risk = predict_outcome(form_data)
        #if CHD_risk == 1:
            #print("you are at high risk of heart disease")
        #else:
            #print("you are not at high risk of heart disease")
    
    # print(np.array(form_data))
    result = predict_outcome(np.array(form_data).reshape(-1,11))
    # print(result)

    if (sex == "Male" and age >50):
        non_ml_result = "Unusual"
    else:
        non_ml_result  = "No Result"
        

    # return jsonify(form_data) 
    return render_template('results.html', results_output = result, Age =  age, Sex = sex_raw, SysBP = Systolic_BP, Cholesterol = chol, Glucose = glucose, 
    BMI = bmi, Resting_HR = restingHR, Cigs = cigs, Education = education_raw, BP_Medication = bpMed_raw, Stroke = stroke_raw, non_ml_output =  non_ml_result  )
    # return(form_data)

if __name__=="__main__":
    app.run(debug=True)