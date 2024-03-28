import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache(allow_output_mutation=True)
def load_data():
    return pd.read_csv('unicorns.csv', encoding='utf-8', delimiter=',')

def pre_process(df):
    df = df.drop(['id', 'date_joined'], axis=1)
    df['date_founded'] = pd.to_datetime(df['date_founded'])
    # force the founders column to be strings
    df['founders'] = df['founders'].astype(str)
    return df

# Compute the number of founders
def count_founders(founders):
    return len(founders.split(','))

st.title('Unicorn companies')

df = load_data()
df = pre_process(df)

if st.sidebar.checkbox("Only companies with female founders", value=False):
    df = df[df['female_founders'] == 'Yes']

type_of_plot = st.sidebar.radio("Type of plot",
    ['Scatter plot', 'Strip plot', 'Box plot'])

# Add a new column with the number of founders
df['number_founders'] = df['founders'].apply(count_founders)

# Plot funding rounds by number of founders
fig, ax = plt.subplots(figsize=(6.4, 2.4))

if type_of_plot == 'Scatter plot':
    sns.scatterplot(data=df, x='number_founders', y='funding_rounds')
elif type_of_plot == 'Strip plot':
    sns.stripplot(data=df, x='number_founders', y='funding_rounds')
elif type_of_plot == 'Box plot':
    sns.boxplot(data=df, x='number_founders', y='funding_rounds')

ax.grid(axis='y') # horizontal grid lines
ax.set_xlabel('Number of founders')
ax.set_ylabel('Funding rounds')
ax.set_title('Funding rounds by number of founders')

st.pyplot(fig)