import pandas as pd
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
# Training pipeline :-
housing_prepared = final_pipeline.fit_transform(housing)
housing_features = final_pipeline.get_feature_names_out()
housing_prepared=pd.DataFrame(housing_prepared,columns=housing_features,index=housing.index)

# Testing pipeline :-
test_labels=test_set["median_house_value"].copy()
test_set=test_set.drop("median_house_value",axis=1)
new_test2=final_pipeline.fit_transform(test_set)
new_features =final_pipeline.get_feature_names_out()
new_test2=pd.DataFrame(new_test2,columns=new_features,index=test_set.index)

# Linear Regression 
lin_reg=LinearRegression()
lin_reg.fit(housing_prepared,housing_labels)
lin_pre=lin_reg.predict(new_test2)
lin_rmse=root_mean_squared_error(test_labels,lin_pre)
print("Linear Regression :",int(lin_rmse))

# Decision Tree :-
dec_tree=DecisionTreeRegressor(random_state=42)
dec_tree.fit(housing_prepared,housing_labels)
dec_pre=dec_tree.predict(new_test2)
dec_rmse=root_mean_squared_error(test_labels,dec_pre)
print("Decision Tree :",int(dec_rmse))

# Random Forest :-
ran_for=RandomForestRegressor()
ran_for.fit(housing_prepared,housing_labels)
ran_pre=ran_for.predict(new_test2)
ran_rmse=root_mean_squared_error(test_labels,ran_pre)
print("Random Forest :",int(ran_rmse))