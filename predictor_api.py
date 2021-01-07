import joblib

# create function under predictor_api
def predict_outcome(form_data):
    # C:\Users\Ryan\Desktop\final_project_new\CHD_predictor\web_pg\static\models
    predictor = joblib.load('./static/models/knn_model.sav')
    output = predictor.predict(form_data)

    print(output)

    if output == 1: 
        outputnorm = "High Risk"
    else:
        outputnorm = "Low Risk"

    return outputnorm
