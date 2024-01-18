import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline  # Add this import
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'proprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ['instant', 'season', 'yr', 'mnth', 'holiday', 'weekday',
                                  'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed',
                                  'casual', 'registered']
            target_column_name = 'cnt'

            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, numerical_columns)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_object()

            x = train_df.drop(columns=['cnt','dteday'],axis=1)
            y = train_df['cnt']

            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            x_train_transformed = preprocessing_obj.fit_transform(x_train)
            x_test_transformed = preprocessing_obj.transform(x_test)

            logging.info(f"Applying StandardScaler on transformed data.")

            sc = StandardScaler()
            x_train_transformed = sc.fit_transform(x_train_transformed)
            x_test_transformed = sc.transform(x_test_transformed)

            logging.info(f"Saved preprocessing object.")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                x_train_transformed,
                x_test_transformed,
                y_train,
                y_test,
                self.data_transformation_config.preprocessor_obj_file_path,
            )

        except Exception as e:
            raise CustomException(e, sys)
