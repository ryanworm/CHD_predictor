# Predictive Analytics

This application identifies risk individual risk catagories for coronary heart disease.   

* Data downloaded from https://www.kaggle.com/amanajmera1/framingham-heart-study-dataset
* Used pandas to read in CSV dataset (n=4240)
* Cleaned data of any partial datasets (n=645)
* Data processing
 * To ensure that the training data contained enough positive CHD data the dataset was upscaled (n=6202).
 * In order to create a more reliable model the like attributes were removed. This was done through a seaborn heatmap by comparing highly correlated attributes. Overlapping catagories such as "Smoker" and "Cigarettes" were deemed redundant and the binary option was removed. This allowed the attribute to have a magnitude and improved prediction accuracy.  
* Machine Learning
  * Training the models
  * Picking our model
* Scoring of our model

# Tools/Packages Used
* Numpy
* Pandas
* Seaborn
* Matplotlib
* TensorFlow
* Joblib

# How to use:
* Click on *Health Intake* header to the top right
* Input your information 
* Click submit
* The results page will display your risk catagory (Hight/Low) as well as identifying personal risk factors based on your intake form. 


Available on Heroku: https://predictivehealth.herokuapp.com/static/html/index.html




