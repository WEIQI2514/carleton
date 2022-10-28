import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache()
def load_data():
    return pd.read_csv('unicorns.csv', encoding='utf-8', delimiter=',')

def pre_process(df):
    df = df.drop(['id', 'date_joined'], axis=1)
    df['date_founded'] = pd.to_datetime(df['date_founded'])
    return df

st.title('Funding by company')
df = load_data()
df = pre_process(df)
if st.sidebar.checkbox("Show the data", value=False):
    st.write(df)

# Funding amounts by company, sorted by amount
st.subheader("Funding amounts by company")
df_sorted = df.sort_values('funding', ascending=False)

fig, ax = plt.subplots(figsize=(6.4, 2.4))

sns.lineplot(x='company', y='funding', data=df_sorted, ax=ax)

ax.set_xlabel('Company (in order of funding received)')
ax.set_ylabel('Funding')

# Show index of companies as labels on x-axis
# Only show every 20th label
ax.set_xticks(np.arange(0, len(df_sorted), 20))
ax.set_xticklabels(np.arange(0, len(df_sorted), 20), rotation=45)
ax.grid(axis='y') # horizontal grid lines

st.pyplot(fig)