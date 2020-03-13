#import dash_core_components as dcc
#import dash_html_components as html
#import numpy as np
#import matplotlib.pyplot as plt
#import io
#from sklearn.metrics import mean_absolute_error
#from sklearn import svm
#from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.linear_model import LogisticRegression


def datapreprocessing():
    heart = pd.read_csv('framingham.csv', sep=',', header=0)
    heart = heart.rename(index=str, columns={'male': 'Gender', 'age': 'Age', 'BPMeds': 'Blood_Pressure_Medication'})

    # Cleaning the data which having NA values by removing the null valued rows
    heart = heart.dropna()
    # Remove duplicate values from the database
    heart = heart.drop_duplicates(subset=['Gender', 'Age', 'currentSmoker', 'cigsPerDay',
                                          'Blood_Pressure_Medication', 'prevalentStroke', 'prevalentHyp',
                                          'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose',
                                          'TenYearCHD'], keep='first')
    # Drop the values which doesn't affect the results
    heart = heart.drop(['education', 'Blood_Pressure_Medication', 'prevalentStroke', 'diabetes', ], axis=1)

    # Normalize the data which in betwenn 0 & 1
    heart['Age'] = (heart['Age'] - heart['Age'].min()) / (heart['Age'].max() - heart['Age'].min())
    heart['cigsPerDay'] = (heart['cigsPerDay'] - heart['cigsPerDay'].min()) / (
                heart['cigsPerDay'].max() - heart['cigsPerDay'].min())
    heart['totChol'] = (heart['totChol'] - heart['totChol'].min()) / (heart['totChol'].max() - heart['totChol'].min())
    heart['sysBP'] = (heart['sysBP'] - heart['sysBP'].min()) / (heart['sysBP'].max() - heart['sysBP'].min())
    heart['diaBP'] = (heart['diaBP'] - heart['diaBP'].min()) / (heart['diaBP'].max() - heart['diaBP'].min())
    heart['BMI'] = (heart['BMI'] - heart['BMI'].min()) / (heart['BMI'].max() - heart['BMI'].min())
    heart['heartRate'] = (heart['heartRate'] - heart['heartRate'].min()) / (
                heart['heartRate'].max() - heart['heartRate'].min())
    heart['glucose'] = (heart['glucose'] - heart['glucose'].min()) / (heart['glucose'].max() - heart['glucose'].min())
    return heart


def PreditLR(input):
    heart= datapreprocessing()
    # LOGISTIC REGRESSION

    # Specifying the training dataset
    logReg_y = heart.iloc[:2900, 11]
    logReg_x = heart.iloc[:2900, :11]

    # Training the algorithm
    LR = LogisticRegression(random_state=0, solver='lbfgs', multi_class='ovr').fit(logReg_x, logReg_y)
    answer = LR.predict(input)
    return answer
   # return 1


# if __name__ == '__main__':
#     # input_values should be taken as user input. This is only sample case.
#     input_values = [[1,10,0,1,20,30,40,50,60,70,80]]
#     Ans = PreditLR(input_values)
#     print(Ans)
