import os
import pickle

import pandas as pd
from sklearn import linear_model

csv_file = os.getenv("CSV_FILE")
model_file = os.getenv("MODEL_FILE", "model.pkl")

df = pd.read_csv(csv_file)
y = df["Value"]  # dependent variable
x = df[["Rooms", "Distance"]]  # independent variable
x = x.values  # conversion of X into array

print(f"Shape : {df.shape}")  # show dimensions of dataset
print(f"Info : {df.info}")  # show dimensions of dataset
# print(f"Statistical summary: {df.describe()}")
# print(df.head(10))                 # peek the data
# print(df.groupby('Rooms').size())  # Distribution

lm = linear_model.LinearRegression()
lm.fit(x, y)

print(f"Model score : {lm.score(x, y)}")
print(f"Model coefficients : {lm.coef_}")
print(f"Model intercept : {lm.intercept_}")
print(f"Model predict : {lm.predict([[15, 61]])}")  # format of input

pickle.dump(lm, open(model_file, "wb"))  # serialize and save the model to the file
print("Created model file : ", model_file)
