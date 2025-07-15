import os
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score

MODEL_FILE="model.pxl"
PIPELINE_FILE="pipeline.pkl"

def built_pipeline(nums_features,cat_features):
        # Making pipelines for numerical value .
    nums_pipeline=Pipeline([
        ("imputer",SimpleImputer(strategy="median")),
        ("scaler",StandardScaler())
    ])

    # Making pipeline for categotical data .
    cat_pipeline=Pipeline([
        ("one_hot_encoder",OneHotEncoder(handle_unknown="ignore"))
    ])

    # Making the final pipeline .
    final_pipeline = ColumnTransformer([
        ("nums",nums_pipeline,nums_features),
        ("cat",cat_pipeline,cat_features)
    ])
    return final_pipeline

if not os.path.exists(MODEL_FILE):
    # Loading the data set to the program . 
    df =pd.read_csv("housing.csv")

    # Creating a stratified test set .
    df["income_cat"]=pd.cut(df["median_income"],bins=[0,1.5,3.0,4.5,6.0,np.inf],labels=[1,2,3,4,5])
    split=StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)

    for train_index,test_index in split.split(df,df["income_cat"]):
        if not os.path.exists("input.csv"):
            df.loc[test_index].drop("income_cat",axis=1).to_csv("input.csv")
        df_train=df.loc[train_index].drop("income_cat",axis=1)

    # Making copy of the training data set .
    housing = df_train.copy()

    # Seprating the Features and Labels .
    housing_labels = housing["median_house_value"]
    housing_features = housing.drop("median_house_value",axis=1)

    # Seprating numerical and categorical data .
    nums_features=housing_features.drop("ocean_proximity",axis=1).columns.tolist()
    cat_features=["ocean_proximity"]

    pipeline=built_pipeline(nums_features,cat_features)
    housing_prepared=pipeline.fit_transform(housing_features)

    model = RandomForestRegressor(random_state=42)
    model.fit(housing_prepared,housing_labels)

    joblib.dump(model,MODEL_FILE)
    joblib.dump(pipeline,PIPELINE_FILE)

    print("Model has been trained successfully ")

else :
    model = joblib.load(MODEL_FILE)
    pipeline=joblib.load(PIPELINE_FILE)

    input_data = pd.read_csv("input.csv")
    transformed_input=pipeline.transform(input_data)

    predictions=model.predict(transformed_input)
    input_data["median_house_value"]=predictions

    input_data.to_csv("output.csv",index=False)
    print("Inference is done succesfully and saved file to {output.csv} file ")
    print(pd.read_csv("output.csv"))