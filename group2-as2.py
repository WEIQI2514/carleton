import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import imblearn


from numpy import mean
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.impute import SimpleImputer
from sklearn.inspection import PartialDependenceDisplay
from sklearn.preprocessing import StandardScaler, OneHotEncoder    
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn import metrics
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline


#for visiualizing pipelines
from sklearn.utils import estimator_html_repr
import streamlit.components.v1 as components

st.title('TIM5301 Assignment 2 (Group-2)')

# Load cruchbase dataset
@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv('crunchbase.csv')
    return df


# DATA UNDERSTANDING AND PREPARATION
# Checklist:
# Identify a suitable range of data to use
# Select a target (or create a target)
# Create derived features from existing features
# Identify numerical features and their correlations
# Identify categorical features
# Check for look-ahead bias(data leakage)
# Check for missing values
# Check for duplicate rows
# Check for class imbalance

st.title('Crunchbase Data')
df = load_data()


# Identify a suitable range of data to use
# companies age from 3-7 years
def pre_process(df):
    df['age_year']=df['age']/365
    df = df[(df['age_year'] >3 ) & (df['age_year'] < 7)]
    df = df.drop('age',axis=1)
    return df

df = pre_process(df)
num_companies=df.count()[0]
st.dataframe(df)

if st.sidebar.checkbox("dataset after preprocessing"):
    st.subheader("Data set after preprocessing")
    st.write(df)
    st.write('Number of companies remaining is :' , num_companies)
    

# Calculate the number of companies greater than 3 years and younger than 7 years
df.shape

# Select a target (or create a target)
# Map ipo or is_acquired ==True ->success, is_closed & else ->no

def success_test(ipo, is_acquired, is_closed):
#df = df[((df['ipo'] == True ) | (df['is_acquired'] == True)) & (df['is_closed'] == False)]
    if is_closed == True:
        return 0
    elif (ipo==False) and (is_acquired==False)  and (is_closed==False):
        return 0
    else:
        return 1

# Apply success function to each row (axis=1) 

df['success'] = df[['ipo','is_acquired','is_closed']].apply(lambda x : success_test(*x), axis=1)

# drop raw features
#df = df.drop('ipo', axis=1)
#df = df.drop('is_acquired', axis=1)
#df = df.drop('is_closed', axis=1)

# Create derived features from existing features
# no feature refers to the eduction levels of founders, so create a new feature (number_degrees)
# that is sum of the degrees


column_names = ['mba_degree', 'phd_degree', 'ms_degree', 'other_degree']
df['number_degrees']= df[column_names].sum(axis=1)

#if st.sidebar.checkbox("Show derived features"):
#    st.header('Derived features')
#    st.write(df)

# drop raw features
#df = df.drop('mba_degree', axis=1)
#df = df.drop('phd_degree', axis=1)
#df = df.drop('ms_degree', axis=1)
#df = df.drop('other_degree', axis=1)


# Identify numerical features and their correlations
# Ask pandas to give us the numerical columns

numerical_features = df.select_dtypes(include=np.number).columns
print(numerical_features)

numerical_features = ['average_funded', 'total_rounds', 'average_participants','products_number','offices','acquired_companies', 'age_year','number_degrees']
numerical_features_and_target = numerical_features + ['success']

if st.sidebar.checkbox("Show correlation matrix"):
    st.subheader("Correlation matrix")

# Show the correlations of the numerical features with one another and with the target
    fig, ax = plt.subplots(figsize=(12.8, 9.6))
    sns.heatmap(df[numerical_features_and_target].corr(), annot=True, fmt=".2f", ax=ax)
    ax.set_title("Correlations of numerical features and target")
    st.pyplot(fig)

# Identify categorical features
categorical_features = ['country_code','state_code','ipo','is_acquired','is_closed']

# Check for look-ahead bias (data leakage)
# all features are known before the investment is made, so we don't have look-ahead bias.
# In our dataset, I am not sure about whether ‘average_funded’ and ‘total_rounds’ include the ipo. 

# Check for missing values
def missing_values_ratios(df):
    # Calculate the ratio of missing values in each column
    return df.isna().sum() / len(df)

if st.sidebar.checkbox("Show missing values ratios"):
    st.subheader("Missing values ratios")
    st.write(missing_values_ratios(df))

# There are missing values in columns:['category_code','average_funded','average_funded',
#'products_number','offices', 'acquired_companies', 'mba_degree','phd_degree','ms_degree',
#'other_degrees] in this dataset
# we can choose default values as 0 for numerical features.
# However we cannot set a default value for category_code

# Check for duplicate rows
# Count the number of duplicate rows
num_duplicate_rows = df.duplicated().sum()
if st.sidebar.checkbox("Duplicate rows"):
    st.subheader('Number of duplicate rows')
    st.write("%d rows are duplicates" % (num_duplicate_rows))

# Drop duplicates
# There are 2 duplicate rows, so this may not make much difference to our output,but we better remove them.
df = df.drop_duplicates()

# Some features are not informative and should be removed? Which ones?

    
# Check for class imbalance
if st.sidebar.checkbox('Class imbalance'):
    st.subheader('Class imbalance')
    counts = df['success'].value_counts()
    
    fig, ax = plt.subplots(figsize=(4.8, 2.4))
    sns.barplot(x=counts.index, y=counts.values, ax=ax)
    ax.set_xticklabels(['No', 'Yes'])
    ax.set_xlabel('Success of startup')
    ax.set_ylabel('Number of startup')
    ax.set_title('Class imbalance')
    st.pyplot(fig)

    successful_startups = counts[1]
    failed_startups = counts[0]
    st.write('Degree of imbalance: %.1f to 1 failed startup to successful startup' % 
        (failed_startups/successful_startups))

# MODELING
# Checklist:
# Create a pipeline for pre-processing features
# Create a pipeline for training the model

# Create a pipeline for pre-processing features
# This should also take care of missing values (here, there are 'average_funded','average_funded',
#'products_number','offices', 'acquired_companies', 'mba_degree','phd_degree','ms_degree',
#'other_degrees should assign default value;'category_code' fill missing in.


def pre_processor(numerical_features, categorical_features):
    # Pipeline for pre-processing numeric features
    # Scale all values to zero mean and unit variance (many algorithms assume this)
    # As we had missing values, we use SimpleImputer here
    numerical_transformer = Pipeline(
        steps = [('imputer', SimpleImputer(strategy='constant', fill_value=0)),
                 ('scaler', StandardScaler())])

        # Pipeline for pre-processing categorical features
    # One-hot encode the values
    categorical_transformer = Pipeline(
        steps = [('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
                 ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    # Combine the two pipelines into one
    preprocessor = ColumnTransformer(
        transformers = [('num', numerical_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)])
    # Also return a handle to the one-hot encoder (needed for feature importance)
    return preprocessor

# Create a pipeline for training the model
preprocessor = pre_processor(numerical_features, categorical_features)
type_of_classifier = st.sidebar.radio("Select type of classifier", 
    ("Decision Tree", "Random Forest","Logistic Regression", "Gradient Boosting", "Neural Network"))
if type_of_classifier == "Decision Tree":
    classifier = DecisionTreeClassifier(max_depth=3, class_weight='balanced')
elif type_of_classifier == "Random Forest":
    classifier = RandomForestClassifier(n_estimators = 100, random_state = 42)
elif type_of_classifier == "Logistic Regression":
    classifier = LogisticRegression(max_iter=2000, penalty='l2', class_weight='balanced')
elif type_of_classifier == "Gradient Boosting":
    classifier = GradientBoostingClassifier()
elif type_of_classifier == "Neural Network":
    classifier = MLPClassifier(max_iter=2000, hidden_layer_sizes=(30,), early_stopping=True)
model = Pipeline(steps=[('preprocessor', preprocessor),
    ('classifier', classifier)])

# Show the pipeline
if st.sidebar.checkbox("Show pipeline"):
    st.subheader("Pipeline")
    components.html(estimator_html_repr(model), height=500)


# EVALUATION
# Checklist:
# Choose train and test datasets (stratified? time-split?)
# Identify the most suitable performance metrics for evaluating the model
# Choose a way to deal with imbalanced data
# Use k-fold cross-validation to evaluate the model (stratified? time-split?)
# Fit and evaluate the model against the test dataset
# Rank the features by their importance

X = df.drop('success', axis=1)
y = df['success']

# Choose train and test datasets
# When the samples are independent, create a stratified split
# Split the data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, shuffle=True, stratify=y, random_state=42)


# Identify the most suitable performance metrics for evaluating the model
# The classes are imbalanced, so we would use the F1 score which balances precision and recall
# However, there may be better metrics for a specific problem

## As suggested by Moro et al.,
# Use k-fold cross-validation to evaluate the model
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_validate(model, X_train, y_train, cv=cv, n_jobs=-1,
  scoring=['accuracy', 'roc_auc', 'precision', 'recall', 'f1'])

# Choose a way to deal with imbalanced data
# General strategies:
# We can use class weights to balance the classes
# We can also oversample the minority class or undersample the majority class
# Here, we will use Undersampling

# example of evaluating a decision tree with random undersampling
from numpy import mean
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from imblearn.pipeline import Pipeline
from imblearn.under_sampling import RandomUnderSampler
# define dataset
X, y = make_classification(n_samples=9398, weights=[0.08],flip_y=0)
print(Counter(y))
# define pipeline
steps = [('under', RandomUnderSampler()), ('model', DecisionTreeClassifier())]
pipeline = Pipeline(steps=steps)
# evaluate pipeline
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
scoresF1 = cross_val_score(pipeline, X, y, scoring='f1_micro', cv=cv, n_jobs=-1)
scoreF1 = mean(scoresF1)
print('F1 Score: %.3f' % scoreF1)


model.fit(X_train,y_train)
y_pred = model.predict(X_test)
    

if st.sidebar.checkbox("Show Confusion matrix"):
    st.subheader("Confusion matrix")

    conf_matrix = metrics.confusion_matrix(y_test, y_pred)
    
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    sns.heatmap(conf_matrix, annot=True, fmt='d', ax=ax,
    cmap=plt.cm.Greens)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title('Confusion matrix')
    ax.xaxis.set_ticklabels(['No', 'Yes'])
    ax.yaxis.set_ticklabels(['No', 'Yes'])
    st.pyplot(fig)

# Use k-fold cross-validation to evaluate the model
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_validate(model, X_train, y_train, cv=cv, n_jobs=-1,
                        scoring=['accuracy', 'roc_auc', 'precision', 'recall', 'f1'])

if st.sidebar.checkbox("Show model performance (cross validation)"):
    st.subheader('Model performance (cross validation)')
# Performance scores for each fold
st.write("Scores for each fold (only positive class):")
df_scores = pd.DataFrame(scores).transpose()
df_scores['mean'] = df_scores.mean(axis=1)
st.dataframe(df_scores)

# Get feature names
# Optional: set verbose_feature_names_out to False
model.named_steps['preprocessor'].verbose_feature_names_out=False
feature_names = \
              model.named_steps['preprocessor'].get_feature_names_out()

# Get feature importance from the model
feature_importance = \
                   model.named_steps['classifier'].feature_importances_
# Create a dataframe with the feature names and their importance
feature_importance = pd.DataFrame({'feature': feature_names,
                                   'importance': model['classifier'].feature_importances_})
feature_importance = feature_importance.sort_values('importance',ascending=False)
feature_importance = feature_importance.head(10)

# Plot the feature importance as horizontal bar chart
fig, ax = plt.subplots(figsize=(6.4, 4.8))
sns.barplot(x='importance', y='feature', data=feature_importance,
ax=ax, color='blue')
ax.set_xlabel('Feature importance')
ax.set_ylabel('Feature')
ax.set_title("Feature importance")
st.pyplot(fig)


