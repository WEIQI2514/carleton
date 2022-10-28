import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load cruchbase data
@st.cache(allow_output_mutation=True)
def load_data():
    return pd.read_csv('crunchbase.csv',sep=";")

st.title('Startups success prediction')

# DATA UNDERSTANDING AND PREPARATION
# Checklist:
# Identify a suitable range of data to use
# Select a target (or create a target)
# Create derived features from existing features
# Identify numerical features and their correlations
# Identify categorical features
# Check for look-ahead bias (data leakage)
# Check for missing values
# Check for duplicate rows
# Check for class imbalance

df = load_data():
    

# Identify a suitable range of data to use
# NA

# Select a target (or create a target)
# Map yes -> 1, no -> 0
def success(row):
    if row['y'] == 'yes':
        return 1
    else:
        return 0
#education level of the funders
    


