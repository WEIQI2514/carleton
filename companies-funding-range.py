import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

@st.cache(allow_output_mutation=True)
def load_data():
    return pd.read_csv('unicorns.csv', encoding='utf-8', delimiter=',')

def pre_process(df):
    df = df.drop(['id', 'date_joined'], axis=1)
    df['date_founded'] = pd.to_datetime(df['date_founded'])
    return df

# Put funding values into funding ranges
# Funding amounts are in buckets of 1B
def funding_range(funding):
    if funding < 1e-3:
        return '< 1M'
    elif funding < 1e-2:
        return '1M - 10M'
    elif funding < 5e-2:
        return '10M - 50M'
    elif funding < 1e-1:
        return '50M - 100M'
    elif funding < 5e-1:
        return '100M - 500M'
    elif funding < 1:
        return '500M - 1B'
    elif funding < 10:
        return '1B - 10B'
    else:
        return '> 10B'

st.title('Companies by funding range')
df = load_data()
df = pre_process(df)
if st.sidebar.checkbox("Show the data", value=False):
    # use streamlit to display the dataframe
    st.write(df)

df['funding_range'] = df['funding'].apply(funding_range)
df_funding_ranges = df.groupby('funding_range').count()['company']

funding_range_labels = ['< 1M', '1M - 10M', '10M - 50M',
    '50M - 100M', '100M - 500M', '500M - 1B', '1B - 10B', '> 10B']

fig, ax = plt.subplots(figsize=(6.4, 2.4))

# sns barplot ordered by < 1M, 1M - 10M, 10M - 50M, 50M - 100M, 
#     100M - 500M, 500M - 1B, 1B - 10B, > 10B
sns.barplot(x=df_funding_ranges.index, y=df_funding_ranges.values,  
    color='black', order=funding_range_labels)

# use the labels we defined above
ax.set_xticklabels(funding_range_labels, rotation=45)
ax.grid(axis='y') # horizontal grid lines
ax.set_xlabel('Funding range')

st.pyplot(fig)