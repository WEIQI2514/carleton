import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Load the data and cache it
@st.cache(allow_output_mutation=True)
def load_data():
    return pd.read_csv('unicorns.csv', encoding='utf-8', delimiter=',')

# Pre-process the data
def pre_process(df):
    df = df.drop(['id', 'date_joined'], axis=1)
    df['date_founded'] = pd.to_datetime(df['date_founded'])
    return df

st.title('Companies by country')
df = load_data()
df = pre_process(df)
if st.checkbox("Show the data"):
    # use streamlit to display the dataframe
    st.write(df)

st.write("""
There are multiple ways to do this. In the first approach, we will group the data by country 
and count the number of companies in each country, then use a bar plot to plot the data.
""")
# group the data by country and count the number of companies in each country
df_country = df.groupby('country').count()['company']
# sort the data by number of companies in descending order
df_country = df_country.sort_values(ascending=False)
# default figure size is 6.4 x 4.8
fig, ax = plt.subplots(figsize=(6.4, 2.4))
# bar plot in seaborn, use black color
sns.barplot(x=df_country.index, y=df_country.values, color='black')
ax.set_xlabel('Country')
ax.set_ylabel('Count')
ax.set_title('Companies by country')
plt.xticks(rotation=90)
ax.grid(axis='y') # horizontal grid lines
st.pyplot(fig)

st.write("""
In the second approach, we will use a count plot, which is a bar plot that shows the 
number of observations in each category. We can set the order of the countries using the order parameter.
""")
# count plot of companies by country sorted by count
# use seaborn to plot the count plot
fig, ax = plt.subplots(figsize=(6.4, 2.4))
# count plot already counts the number of companies in each country
# we still need pandas.DataFrame.value_counts to sort them
sns.countplot(x='country', data=df, order=df['country'].value_counts().index)
ax.set_xlabel('Country')
ax.set_ylabel('Count')
ax.set_title('Companies by country')
# rotate the x-axis labels by 90 degrees
plt.xticks(rotation=90)
st.pyplot(fig)
