import joblib
import pandas as pd
import os
import numpy as np
from matplotlib import pyplot
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

MODEL_FILE="model.pxl"
PIPELINE_FILE="pipeline.pxl"

def built_pipeline(housing_num,housing_cat):
        
    # Creating a pipeline for numerical value
    pipeline_num=Pipeline([
        ("Imputer",SimpleImputer()),
        ("StandardScaler",StandardScaler())
    ])

    # Creating a pipeline for object data 
    pipeline_cat=Pipeline([
        ("OneHotEncoder",OneHotEncoder(handle_unknown="ignore"))
    ])

    # Creating a final pipeline 
    final_pipeline=ColumnTransformer([
        ("Numerical",pipeline_num,housing_num),
        ("Categorical",pipeline_cat,housing_cat)
    ])
    return final_pipeline

if not os.path.exists(MODEL_FILE):
        
    # Loading the data 
    main_data =pd.read_csv("housing.csv")

    # Creating a new column named - {income_cat}
    main_data["income_cat"]=pd.cut(main_data["median_income"],bins=[0,1.5,3.0,4.5,6.0,np.inf]
                            ,labels=[1,2,3,4,5])

    # Startified Shuffling the main_data 
    model_split=StratifiedShuffleSplit(n_splits=1,random_state=42,test_size=0.2)
    for train_indices,test_indices in model_split.split(main_data,main_data["income_cat"]):
        train_set=main_data.loc[train_indices].drop("income_cat",axis=1)
        test_set=main_data.loc[test_indices].drop("income_cat",axis=1)

    # Creating features and labels from train_set
    housing_labels=train_set["median_house_value"].copy()
    housing = train_set.drop("median_house_value",axis=1)

    # Seprating the numerical and object column from the housing (ie.,train_set)
    housing_num=housing.select_dtypes(include=np.number).columns.tolist()
    housing_cat=housing.select_dtypes(include=np.object_).columns.tolist()

    pipeline = built_pipeline(housing_num,housing_cat)
    housing_prepared=pipeline.fit_transform(housing)

    model =RandomForestRegressor()
    model.fit(housing_prepared,housing_labels)

    joblib.dump(model,  MODEL_FILE) 
    joblib.dump(pipeline,  PIPELINE_FILE) 

    print("Model trained and saved successfully")

else:
    model =joblib.load("model.pxl")
    pipeline = joblib.load("pipeline.pxl")

    input_data=pd.read_csv("input.csv")
    transformed_data =pipeline.fit_transform(input_data)
    prediction=model.predict(transformed_data)
    input_data["median_house_value"]=prediction
    input_data.to_csv("Output.csv")
    print("Inference is successfully done \nOutput : output.csv")
