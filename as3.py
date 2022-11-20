import pandas as pd
import streamlit as st
import matplotlib.pylot as plt
import seaborn as sns
import numpy as np
import json

st.title("Group_2_assignment3")

#Fetch tweets related to "Haribo" using a command:
#snscrape --jsonl --progress --max-results 500 --since 2022-10-01 twitter-seach "#haribo until:2022-10-31" >haribo.json

def load_data():
    #Read one twitter per line from haribo.json
    with open("haribo.json","r") as f:
        tweets = f.readlines()
        # Covert json string to dictionary
        tweets = [json.loads(tweet) for tweet in tweets]
        return tweets
    
tweets = load_data()
# Map json keys to dictionary keys
