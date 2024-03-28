# Scikit-learn examples

# Requirements:
# Libraries required: scikit-learn, pandas, numpy, and streamlit
# To install any of these libraries, run the following command on the command line:
# python3 -m pip install <library_name>

# Running the script:
# To run the script, run the following command on the command line:
# streamlit run scikit-learn.py
# Running this will open a new browser window with the streamlit app

# To learn more about streamlit, visit:
# https://streamlit.io

import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest
from sklearn import metrics

# We need some data to work with
def load_data():
    return pd.read_csv("bank-additional-full.csv", sep=";")

# Read the data and separate features X from target y
df = load_data()
X = df.drop('y', axis=1)
y = df['y']

# For this example, we will only use a subset of the features
# Logistic regression requires numerical features
# In class, we will discuss how to handle categorical features
# Suppose, we are interested in understanding the impact of social and 
# economic factors on the success of a marketing campaign
X = X[['emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']]
st.caption("Features")
st.dataframe(X)

# Split the data into train and test sets
# Here we use 80% of the data for training and 20% for testing
# We also shuffle the data (which is enabled by default)
# In class, we discussed that this is not always a good idea,
# especially when the data is ordered in some way
# For this example, however, we will just use the default settings
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Estimator
clf = LogisticRegression(penalty="l2") 
clf.fit(X_train, y_train)

# Predictor
y_pred = clf.predict(X_test)

# How good is the prediction?
def check_performance(y_test, y_pred):
    score = metrics.classification_report(y_test, y_pred, output_dict=True)
    st.write("Accuracy:", score['accuracy'])
    st.write("Precision:", score['macro avg']['precision'])
    st.write("Recall:", score['macro avg']['recall'])

st.caption("How good is the prediction?")
check_performance(y_test, y_pred)

# Transformer
scaler = StandardScaler() 
scaler.fit(X_train)
X_train = scaler.transform(X_train)

# Redo fit and predict
clf.fit(X_train, y_train)
X_test = scaler.transform(X_test)
y_pred = clf.predict(X_test)

# How good is the prediction now?
st.caption("How good is the prediction now (after scaling)?")
check_performance(y_test, y_pred)

# Turns out that scaling did not make a difference in this case
# However, it often does, so it is a good idea to always scale your data

# Note that we had to transform the test set as well
# Train and test sets should be transformed in the same way
# This is why we use a pipeline to do this automatically

# Pipeline
pipeline = Pipeline([
    ('std_scaler', StandardScaler()),
    ('clf', LogisticRegression(penalty="l2"))])
pipeline.fit(X_train, y_train)

# Now we can just use the pipeline to predict
# The pipeline will automatically scale the test set
y_pred = pipeline.predict(X_test)

# Let's check the performance again
st.caption("Let's check the performance again (now using a pipeline)")
check_performance(y_test, y_pred)

# Suppose we also wanted to select the top 3 features
# We can use a pipeline to do this as well
pipeline = Pipeline([
    ('std_scaler', StandardScaler()),
    ('select_k_best', SelectKBest(k=3)),
    ('clf', LogisticRegression(penalty="l2"))])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# Let's check the performance again
st.caption("How good is the prediction if we use the top 3 features?")
check_performance(y_test, y_pred)

# If you are curious, you can check which features were selected
st.caption("Which features were selected?")
# named_steps is a dictionary that contains the steps in the pipeline
feature_idx = pipeline.named_steps['select_k_best'].get_support(indices=True)
st.write(X.columns[feature_idx])

# It seems that Logistic Regression is already selecting features internally
# In fact, regularization (the penalty above) removes redundant features