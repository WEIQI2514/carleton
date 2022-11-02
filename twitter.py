import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json

st.title("Twitter")

# Fetch tweets using a command like this:
# snscrape --jsonl --progress --max-results 100 --since 2022-10-01 twitter-search "#climatechange until:2022-10-31" >tweets.json
# snscrape --jsonl --progress --max-results 500 --since 2022-07-01 twitter-search "(idea OR #idea) AND (sustainability OR #sustainability) -is:retweet until:2022-09-30"

# Uses the snscrape library to fetch tweets
# https://pypi.org/project/snscrape/

# Construcing a twitter search query
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
# https://www.tweetbinder.com/blog/twitter-advanced-search/

def load_data():
    # Read one tweet per line from tweets.json
    with open("ideas.json", "r") as f:
        tweets = f.readlines()
        # Convert json string to dictionary
        tweets = [json.loads(tweet) for tweet in tweets]
        return tweets

tweets = load_data()
# Map json keys to dictionary keys
# Include only the keys we need (eg date, content, url, hashtags)
tweets = [{k: v for k, v in tweet.items() if k in ['date', 'content', 'url', 'hashtags']} for tweet in tweets]
# This would add all the keys from the json file to the dictionary (which is not what we want)
# tweets = [{k: v for k, v in tweet.items()} for tweet in tweets]
# Convert to dataframe
df_tweets = pd.DataFrame(tweets)
st.write(df_tweets)
