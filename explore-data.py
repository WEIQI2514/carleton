import pandas as pd
import numpy as np

# Load data
def load_data():
    df = pd.read_csv('unicorns.csv')
    return df

# Pre-process data
def pre_process(df):
    for col in ['date_founded', 'date_joined']:
        df[col] = pd.to_datetime(df[col])
    return df

df = load_data()
df = pre_process(df)
st.dataframe(df)
