import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
import csv
import wordcloud



from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import semi_supervised
from sklearn import metrics

# Required for transforming from sparse matrix to dense matrix
from sklearn.base import TransformerMixin

# the gensim library is used for topic modeling
from gensim.models import LdaModel
from gensim.corpora import Dictionary

st.title("Group_2_Assignment3")

# Construcing a twitter search query
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
# https://www.tweetbinder.com/blog/twitter-advanced-search/
# without HTTP：
# has:geo (from:HARIBO OR from:NHC_Atlantic OR from:JeffLindner1) -is:retweet
# with HTTP_cURL command
# curl https://api.twitter.com/2/tweets/search/recent?query=Haribo%20-grumpy&tweet.fields=created_at&max_results=500 -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAADQ3jgEAAAAAO%2BExCzmOqUpLDh3Kt3FzwbSVQtI%3DCdFHOJ4FMAmoGTiukBYzuqFVdQNuAdT9q5xn3w4mI4ocFZaVyC"

# Fetch tweets of haribo candy by using commands below:
# snscrape --jsonl --progress --max-results 500 --since 2022-08-01 twitter-search "(haribo OR #haribo) lang:en -is:retweet until:2022-08-30" >ideas1.json
# snscrape --jsonl --progress --max-results 500 --since 2022-09-01 twitter-search "(haribo OR #haribo) lang:en -is:retweet until:2022-09-30" >ideas2.json


def load_data():
    # Read one tweet per line from ideas1.json
    with open("ideas1.json", "r") as f:
        tweets = f.readlines()
        # Convert json string to dictionary
        tweets = [json.loads(tweet) for tweet in tweets]
        return tweets

tweets = load_data()
# Map json keys to dictionary keys
# Include only the keys we need (eg date, content, url, hashtags)
tweets = [{k: v for k, v in tweet.items() if k in ['date', 'content', 'url', 'hashtags']} for tweet in tweets]
# Convert to dataframe
df_tweets = pd.DataFrame(tweets)
st.write(df_tweets)
#convert the json string to a csv
export_csv = df_tweets.to_csv (r'C:\Users\Vic92\Desktop\as3\ideas1.csv', na_rep='', index = False)

def load_corpus():
    return pd.read_csv("ideas1.csv")

def load_labels():
    return pd.read_csv("tweets-labels.csv")
corpus = load_corpus()
labels = load_labels()

# Merge the labels with the corpus
corpus['label'] = -1 # initialize all labels to -1 (unlabeled)
# Set the labels for the labeled tweets
for _, row in labels.iterrows():
    corpus.loc[row['id'], 'label'] = row['label']

# A tutorial on indexing dataframes with loc is:
# https://towardsdatascience.com/how-to-use-loc-in-pandas-49ed348a4117

if st.sidebar.checkbox("Show corpus"):
    st.subheader("Corpus")
    st.dataframe(corpus)

# Create a term-document matrix
# The term-document matrix is a dataframe with the words as rows and the documents as columns
# Create a pipeline to vectorize the tweets
preprocessor = Pipeline([
    ('vectorizer', CountVectorizer(stop_words='english', max_features=100, min_df=2)),
    ('tfidf', TfidfTransformer())])
tfidf = preprocessor.fit_transform(corpus['content'])
vectorizer = preprocessor.named_steps['vectorizer']
vocab = vectorizer.get_feature_names()
tdm = pd.DataFrame(tfidf.toarray().T, index=vocab)
if st.sidebar.checkbox('Show term-document matrix'):
    st.subheader('Term-document matrix')
    st.write('The rows are words and the columns are documents.')
    st.dataframe(tdm)

# Self-training requires a base estimator
base_estimator = LogisticRegression(penalty='l2', class_weight='balanced')
classifier = semi_supervised.SelfTrainingClassifier(base_estimator)
model = Pipeline(steps=[
    ('vectorizer', CountVectorizer(stop_words='english', min_df=2, max_features=100)),
    ('tfidf', TfidfTransformer()),
    ('classifier', classifier)])

# To use label spreading we need to convert the output of TF-IDF to a dense matrix
# https://stackoverflow.com/questions/28384680/scikit-learns-pipeline-a-sparse-matrix-was-passed-but-dense-data-is-required
class DenseTransformer(TransformerMixin):
    def fit(self, X, y=None, **fit_params):
        return self

    def transform(self, X, y=None, **fit_params):
        return X.todense()

# Can use FunctionTransformer instead of DenseTransformer
# transformer = FunctionTransformer(lambda x: x.todense(), accept_sparse=True)

# classifier = semi_supervised.LabelSpreading()
# model = Pipeline(steps=[
#     ('vectorizer', CountVectorizer(stop_words='english', min_df=2, max_features=100)),
#     ('tfidf', TfidfTransformer()),
#     ('to_dense', FunctionTransformer(lambda x: x.todense(), accept_sparse=True)),
#     ('classifier', classifier)])

# Apply the pipeline to the corpus
# Convert series to dense array
model.fit(corpus['content'], corpus['label'])

# Predict the labels for the corpus
if st.sidebar.checkbox("Predicted labels"):
    st.subheader("Predicted labels")
    # Predict the labels for the unlabeled tweets
    corpus['predicted'] = model.predict(corpus['content'])
    st.dataframe(corpus)
    # Statistics
    st.write("This is a count of the predicted labels:")
    st.write(corpus['predicted'].value_counts())



# model

@st.cache(allow_output_mutation=True)
def load_corpus(file):
	documents = pd.read_csv(file)
	return documents

def read_stopwords(file):
	file = open(file, 'r')
	return [w.strip() for w in file.read().split('\n')]

def remove_hyphens(document):
	return document.replace('- ', '')

def tokenize(document):
	return [w.lower() for w in document.split()]
