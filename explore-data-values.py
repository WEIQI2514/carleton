import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv('unicorns.csv')
    return df

# Pre-process data
def pre_process(df):
    for col in ['date_founded', 'date_joined']:
        df[col] = pd.to_datetime(df[col])
    return df

# Fetch values for categorical columns and [] for numerical columns
def column_values(df):
    values = []
    for col in df.columns:
        # does the column contain categorical data?
        if df[col].dtype == 'object':
            categories = df[col].unique()
            categories = [str(cat) for cat in categories]
            categories.sort()
            values.append(categories)
        # otherwise, there is nothing to see here
        else:
            values.append([])
    return values
    
# Show a summary of the data
# Shows column names, number of unique values, and the values themselves
# for categorical columns, and just the name for numerical columns
def summary(df):
    st.write(pd.DataFrame([df.columns, df.nunique(), column_values(df)], 
        index=['Column', 'Unique', 'Values']).T)

st.title('Explore data and values')
df = load_data()
df = pre_process(df)

# radio button to select the summary or the data
option = st.sidebar.radio('Select an option', ['Data', 'Summary'])

# show the data or the summary
if option == 'Data':
    st.subheader('Data')
    st.write(df)
else:
    st.subheader('Summary')
    summary(df)