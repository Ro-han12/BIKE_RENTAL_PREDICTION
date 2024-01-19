import sys 
import pandas as pd 
from src.exception import CustomException 
from src.utils import load_object

class PredictPipeline():
    def __int__(self):
        pass 
    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            prediction=model.predict(data_scaled)
            return prediction
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
        def __init__(self,
                 instant: int,
                 season: str,
                 yr: int,
                 mnth: int,
                 hr: int,
                 holiday: bool,
                 weekday: str,
                 workingday: int,
                 weathersit: int,
                 temp: float,
                 atemp: float,
                 hum: float,
                 windspeed: float,
                 casual: int,
                 registered: int,
                 cnt: int):
            self.season = season
            self.yr = yr
            self.mnth = mnth
            self.holiday = holiday
            self.weekday = weekday
            self.workingday = workingday
            self.weathersit = weathersit
            self.temp = temp
            self.atemp = atemp
            self.hum = hum
            self.windspeed = windspeed
            self.casual = casual
            self.registered = registered
            

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
                    "atemp": [self.atemp],
                    "hum": [self.hum],
                    "windspeed": [self.windspeed],
                    "casual": [self.casual],
                    "registered": [self.registered]
                }

                return pd.DataFrame(custom_data_input_dict)

            except Exception as e:
                raise CustomException(e, sys)
