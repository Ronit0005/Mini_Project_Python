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

# Loading the data set to the program . 
df =pd.read_csv("housing.csv")

# Creating a stratified test set .
df["income_cat"]=pd.cut(df["median_income"],bins=[0,1.5,3.0,4.5,6.0,np.inf],labels=[1,2,3,4,5])
split=StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)

for train_index,test_index in split.split(df,df["income_cat"]):
    df_test=df.loc[test_index].drop("income_cat",axis=1)
    df_train=df.loc[train_index].drop("income_cat",axis=1)

# Making copy of the training data set .
housing = df_train.copy()

# Seprating the Features and Labels .
housing_labels = housing["median_house_value"]
housing_features = housing.drop("median_house_value",axis=1)

# Seprating numerical and categorical data .
nums_features=housing_features.drop("ocean_proximity",axis=1).columns.tolist()
cat_features=["ocean_proximity"]

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

# Transforming the data .
housing_prepared = final_pipeline.fit_transform(housing_features)
# print(housing_prepared.shape)

# Training the model .

# Linear Regression:-
lin_reg=LinearRegression()
lin_reg.fit(housing_prepared,housing_labels)
lin_predict=lin_reg.predict(housing_prepared)
# lin_rms=root_mean_squared_error(housing_labels,lin_predict)
lin_rms=-cross_val_score(lin_reg,housing_prepared,housing_labels,scoring="neg_root_mean_squared_error",cv=10)
print("Linear Regression",pd.Series(lin_rms).describe())

# Decision Tree :-
dec_tree = DecisionTreeRegressor()
dec_tree.fit(housing_prepared,housing_labels)
dec_predict=dec_tree.predict(housing_prepared)
dec_rms=-cross_val_score(dec_tree,housing_prepared,housing_labels,scoring="neg_root_mean_squared_error",cv=10)
print("Decision tree",pd.Series(dec_rms).describe())

# Random Forest :-
rand_for=RandomForestRegressor()
rand_for.fit(housing_prepared,housing_labels)
rand_predict=rand_for.predict(housing_prepared)
# rand_rms=root_mean_squared_error(housing_labels,rand_predict)
rand_rms=-cross_val_score(rand_for,housing_prepared,housing_labels,scoring="neg_root_mean_squared_error",cv=10)
print("Random forest",pd.Series(rand_rms).describe())
