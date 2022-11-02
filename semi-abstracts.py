import streamlit as st
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

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

# To use SMOTE, we have to use the pipeline implementation from imblearn instead
# from imblearn.pipeline import Pipeline
# from imblearn.over_sampling import SMOTE
# from imblearn.over_sampling import RandomOverSampler

st.sidebar.title("Semi-supervised learning")

def load_corpus():
    corpus = pd.read_csv("abstracts.csv")
    # Combine the title and abstract
    corpus['Content'] = corpus.apply(lambda row: 
        f"{row['Article Title']}. {row['Abstract']}", axis=1)
    # Change column names to lowercase
    corpus.columns = [col.lower() for col in corpus.columns]
    # Sections of the corpus we want to keep
    return corpus[['authors', 'article title', "source title", 'abstract', 
        'content', 'publication year']]

def load_labels():
    return pd.read_csv("abstracts-labels.csv")

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