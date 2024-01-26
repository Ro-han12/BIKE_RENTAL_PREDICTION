import pickle
from flask import Flask,request,render_template
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
application=Flask(__name__)
app=application
#route for home page
@app.route('/predictiondata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        custom_data = CustomData(
            season=request.form.get('season'),
            yr=request.form.get('yr'),
            mnth=request.form.get('mnth'),
            holiday=request.form.get('holiday'),
            weekday=request.form.get('weekday'),
            workingday=request.form.get('workingday'),
            weathersit=request.form.get('weathersit'),
            temp=request.form.get('temp'),
            hum=request.form.get('hum'),
            windspeed=request.form.get('windspeed')
        )

        pred_df = custom_data.get_data_as_data_frame()
        print("Input Data:")
        print(pred_df)  # Print input data for debugging

        predict_pipeline = PredictPipeline()
        print("Before Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")
        print("Prediction Results:")
        print(results)  # Print prediction results for debugging

        return render_template('home.html', results=results[0])

    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True) 
