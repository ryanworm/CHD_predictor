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

@app.route("/request", methods= ['POST'])
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
        totCHO = float(request.form.get('totChol'))
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
        form_data.append((age, sex, sysBP, totCHO, glucose, bmi, restingHR, cigs, education, bpMed, stroke))
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

    #age
    if (age >= 65): 
        non_ml_age = "Increased Risk"
    else: 
        non_ml_age = "Lower Risk"

    #sex
    if (sex == "Male"):
        non_ml_sex = "Increased Risk"
    else:
        non_ml_sex  = "Lower Risk"

    #sysBP
    if (sysBP < 120):
        non_ml_bp = "Low Risk"
    elif (sysBP >= 120 and sysBP <= 129):
        non_ml_bp  = "Increased Risk"
    else: 
        non_ml_bp = "High Risk"

    #cholesterol levels
    if (totCHO <= 200):
        non_ml_CHO = "Low Risk"
    else:
        non_ml_CHO  = "Increased Risk"

    #blood glucose
    if (glucose < 140):
        non_ml_glucose = "Low Risk"
    elif (glucose >= 140 and glucose < 200):
        non_ml_glucose = "Increased Risk"
    else:
        non_ml_glucose = "High Risk"

    #bmi
    if (bmi < 18.5):
        non_ml_bmi = "Increased Risk"
    elif (bmi  >= 18.5 and bmi  <= 24.9):
        non_ml_bmi = "Low Risk"
    elif (bmi >= 25 and bmi <= 29.9):
        non_ml_bmi = "Increased Risk"
    else: 
        non_ml_bmi = "High Risk"

    #heartrate
    if (restingHR < 90):
        non_ml_hr = "Low Risk"
    elif (restingHR >= 90 and restingHR < 100):
        non_ml_hr = "Increased Risk"
    else:
        non_ml_hr = "High Risk"

    #smoking
    if (cigs == 0):
        non_ml_smoking = "Low Risk"
    else: 
        non_ml_smoking = "Increased Risk"

    #education
    if (education <= 2):
        non_ml_education = "Increased Risk"
    else: 
        non_ml_education = "Low Risk"

    #blood pressure
    if (bpMed == 1): 
        non_ml_bpMed = "Increased Risk"
    else: 
        non_ml_bpMed = "Low Risk"

    #previous stroke
    if (stroke == 1):
        non_ml_stroke = "Increased Risk"
    else: 
        non_ml_stroke = "Low Risk"

    # return jsonify(form_data) 
    return render_template('results.html', results_output = result, 
    Age =  age, Sex = sex_raw , Sys_BP = sysBP, 
     totChol = totCHO, glucose = glucose, BMI = bmi, HR = restingHR, Smoking = cigs, Education = education_raw,
     bpMed = bpMed_raw, Prev_stroke = stroke_raw,  
     
     non_ml_age =  non_ml_age, non_ml_sex = non_ml_sex, non_ml_bp = non_ml_bp, 
     non_ml_CHO = non_ml_CHO,  non_ml_glucose =  non_ml_glucose, non_ml_bmi = non_ml_bmi,  non_ml_HR =  non_ml_hr, 
     non_ml_smoking = non_ml_smoking, non_ml_education = non_ml_education, non_ml_bpMed = non_ml_bpMed,  non_ml_stroke =  non_ml_stroke)
    # return(form_data)
   

if __name__=="__main__":
    app.run(debug=True)