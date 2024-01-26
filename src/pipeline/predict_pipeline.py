# import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "proprocessor.pkl")
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 season: int,
                 yr: int,
                 mnth: int,
                 holiday: bool,
                 weekday: int,
                 workingday: bool,
                 weathersit: int,
                 temp: float,
                 hum: float,
                 windspeed: float):
        self.season = season
        self.yr = yr
        self.mnth = mnth
        self.holiday = holiday
        self.weekday = weekday
        self.workingday = workingday
        self.weathersit = weathersit
        self.temp = temp
        self.hum = hum
        self.windspeed = windspeed

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "season": [self.season],
                "yr": [self.yr],
                "mnth": [self.mnth],
                "holiday": [self.holiday],
                "weekday": [self.weekday],
                "workingday": [self.workingday],
                "weathersit": [self.weathersit],
                "temp": [self.temp],
                "hum": [self.hum],
                "windspeed": [self.windspeed]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
