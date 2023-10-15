#!/usr/bin/env python

import argparse
import os
import pickle

import pandas as pd
from sklearn import linear_model

model_file = os.getenv("MODEL_FILE", "model.pkl")

parser = argparse.ArgumentParser()
parser.add_argument("csvfile", type=str, help="Name of the csv file to read from.")


def main(args):
    """Reads csv file from input and performs LinearRegration model serialisation into data file."""
    csv_file = args.csvfile
    df = pd.read_csv(csv_file)

    y = df["Value"]  # dependent variable
    x = df[["Rooms", "Distance"]]  # independent variable
    x = x.values  # conversion of X into array

    print(f"Shape: {df.shape}")  # show dimensions of dataset
    print(f"Info: {df.info}")  # show dimensions of dataset
    print(f"Statistical summary: {df.describe()}")
    # print(df.head(10))                 # peek the data
    # print(df.groupby('Rooms').size())  # Distribution

    lm = linear_model.LinearRegression()
    lm.fit(x, y)

    print(f"Model score: {lm.score(x, y)}")
    print(f"Model coefficients: {lm.coef_}")
    print(f"Model intercept: {lm.intercept_}")
    print(f"Model predict: {lm.predict([[15, 61]])}")  # format of input

    with open(model_file, "wb") as f:
        pickle.dump(lm, f)
        print("Created model file : ", model_file)


if __name__ == "__main__":
    main(parser.parse_args())
