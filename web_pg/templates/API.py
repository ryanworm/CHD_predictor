# contains all the functions to run our model
import pickle
import numpy as np
from sklearn.externals import joblib
import re

def gender_conv(int):
    #converts user input (male/female) to integer value 
    #returns binary value to be evaluated in ML algorithm

def years_edu(int):
    #converts value from drop down to numeric integer to 
    # compare against the model



if __name__ == '__main__':
    from pprint import pprint
    print("Checking to see what empty string predicts")
    print('input string is ')
    form_values = 'bob'
    pprint(chat_in)

    x_input, probs = make_prediction(chat_in)
    print(f'Input values: {x_input}')
    print('Output probabilities')
    pprint(probs)
