## Project: Customer_churn_prediction

## Description: 
The aim of this project is to create an app which will predict that the customer will churn or not based on the clusters. 

## Dataset:
Dataset contains more than 10000 entries.

## Files in this repo:
- model.ipynb
- app.py
- Dockerfile
- requirement.txt

## Workflow:
1. Data cleaning and Data preprocessing: 
  - Remove unnecessary columns
  - Select the features based on correlation using heatmap
  - Perform data scaling with standard scaler
  - Use PCA function to reduce the dimensionality of data
2. Modeling(Clustering model):
  - Use k-means clustreing algorithm to fit the data to the model
3. Create an API:
  - Create a Flask app in app.py file
4. Deploy an app on Heroku:
  - Deploy an app on Heroku using docker

## Usage:

- Install Docker
- Run the folowing commands to build the docker image and to run it
```bash
$ docker build -t flask-heroku
$ docker run -d -p 5000:5000 flask-heroku
```
- Run the following commands to deploy it on heroku
```bash
$ heroku container:login
$ heroku container:push web --app churnprediction-app
$ heroku container:release web --app churnprediction-app
```
