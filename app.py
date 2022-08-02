# Importing all the necessary libraries

from flask import Flask, request, render_template
import joblib
import numpy as np
import os

# Creating app using flask
app = Flask(__name__)

# Loading the model from joblib
model = joblib.load('churn.joblib','r+')

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/predict',methods=['POST'])
def predict():
        Months_on_book = int(request.form['Months_on_book'])
        Total_Relationship_Count = int(request.form['Total_Relationship_Count'])
        Months_Inactive_12_mon = int(request.form['Months_Inactive_12_mon'])
        Contacts_Count_12_mon = int(request.form['Contacts_Count_12_mon'])
        Credit_Limit = float(request.form['Credit_Limit'])
        Total_Revolving_Bal = float(request.form['Total_Revolving_Bal'])
        Total_Amt_Chng_Q4_Q1 = float(request.form['Total_Amt_Chng_Q4_Q1'])
        Total_Trans_Amt = float(request.form['Total_Trans_Amt'])
        Total_Trans_Ct = int(request.form['Total_Trans_Ct'])
        Total_Ct_Chng_Q4_Q1 = float(request.form['Total_Ct_Chng_Q4_Q1'])
        Avg_Utilization_Ratio = float(request.form['Avg_Utilization_Ratio'])
        
        arr = np.array([[Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon,Credit_Limit,Total_Revolving_Bal,Total_Amt_Chng_Q4_Q1,Total_Trans_Amt,Total_Trans_Ct,Total_Ct_Chng_Q4_Q1,Avg_Utilization_Ratio]]) 
        
        prediction = model.predict(arr)
     
        if prediction==0:
             return render_template('result.html',prediction_result="The Customer is belongs to cluster: 0")
        elif prediction==1:
             return render_template('result.html',prediction_result="The Customer is belongs to cluster: 1")
        else:
             return render_template('result.html',prediction_result="The Customer is belongs to cluster: 2")
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", threaded=True, port=port)   