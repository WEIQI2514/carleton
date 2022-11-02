import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets
from sklearn import semi_supervised
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

def load_data():
    return datasets.load_iris()

def show_data(iris):
    X = iris.data
    y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)
    df['target'] = y
    st.write(df)

data = load_data()
st.header("Iris dataset")
show_data(data)

# Keep a copy of the original targets
y_orig = np.copy(data.target)

# Replace 90% of the targets with -1 (unlabelled)
unlabeled_points = np.random.rand(len(y_orig)) < 0.9
data.target[unlabeled_points] = -1

st.subheader("Unlabeled data")
show_data(data)

# Semi-supervised learning
classifier = RandomForestClassifier()
model = semi_supervised.SelfTrainingClassifier(classifier)
# model = semi_supervised.LabelPropagation()
# model = semi_supervised.LabelSpreading()

model.fit(data.data, data.target)
y_pred = model.predict(data.data)

# Classification report
st.subheader("Classification report")
report = metrics.classification_report(y_orig, y_pred, output_dict=True)
df = pd.DataFrame(report).transpose()
st.dataframe(df)
