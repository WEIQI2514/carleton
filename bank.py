import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.model_selection import TimeSeriesSplit
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import StandardScaler, OneHotEncoder    
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn import metrics
from sklearn.inspection import PartialDependenceDisplay

# For visualizing pipelines
from sklearn.utils import estimator_html_repr
import streamlit.components.v1 as components

# load bank dataset
@st.cache(allow_output_mutation=True)
def load_data():
    return pd.read_csv("bank-additional-full.csv", sep=";")

st.title('Bank marketing prediction')

# DATA UNDERSTANDING AND PREPARATION
# Checklist:
# Identify a suitable range of data to use
# Select a target (or create a target)
# Create derived features from existing features
# Identify numerical features and their correlations
# Identify categorical features
# Check for look-ahead bias (data leakage)
# Check for missing values
# Check for duplicate rows
# Check for class imbalance

df = load_data()

# Identify a suitable range of data to use
# NA

# Select a target (or create a target)
# Map yes -> 1, no -> 0
def success(row):
    if row['y'] == 'yes':
        return 1
    else:
        return 0

# Apply success function to each row (axis=1)
df['success'] = df.apply(success, axis=1)

# Remove y column
df = df.drop('y', axis=1)

if st.sidebar.checkbox("Show dataset"):
    st.header('Dataset')
    st.write(df)

# Create derived features from existing features
# pdays: 999 means no previous contact, so create a new feature (contacted)
# that is 1 if pdays is not 999, 0 otherwise
def contacted(pdays):
    if pdays == 999:
        return 0
    else:
        return 1

df['contacted'] = df['pdays'].apply(contacted)
df = df.drop('pdays', axis=1)

if st.sidebar.checkbox("Show derived features"):
    st.header('Derived features')
    st.write(df)

# Identify numerical features and their correlations
# Note: pdays was replaced by contacted
numerical_features = ['age', 'duration', 'campaign', 'contacted', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']
numerical_features_and_target = numerical_features + ['success']

# We could also ask pandas to give us the numerical columns
# numerical_features = df.select_dtypes(include=np.number).columns

if st.sidebar.checkbox("Show correlation matrix"):
    st.subheader("Correlation matrix")
    # Show the correlations of the numerical features with one another and with the target
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    sns.heatmap(df[numerical_features_and_target].corr(), annot=True, fmt=".2f", ax=ax)
    ax.set_title("Correlations of numerical features and target")
    st.pyplot(fig)

# Identify categorical features
categorical_features = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']

# An example of exploratory analysis
if st.sidebar.checkbox('Exploratory analysis'):
    st.subheader('Age distribution with success overlay')
    st.write("""
    The figure overlays success on top of the age histogram. The overlay shows that, proportionally, 
    more younger and older people respond positively when contacted.
    """)
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    sns.histplot(data=df, x='age', hue='success', bins=10, multiple='stack', ax=ax)
    ax.set_title('Age distribution')
    # add legend: 0 -> no, 1 -> yes
    ax.legend(['Yes', 'No'])
    st.pyplot(fig)

# Check for look-ahead bias (data leakage)
# While duration correlates strongly with success, and might be good feature to use from that
# point of view, it is not known before the call is made, so we should remove it
df = df.drop('duration', axis=1)
numerical_features.remove('duration')

# Check for missing values
def missing_values_ratios(df):
    # Calculate the ratio of missing values in each column
    return df.isna().sum() / len(df)

if st.sidebar.checkbox("Show missing values ratios"):
    st.subheader("Missing values ratios")
    # Some features are not informative and should be removed? Which ones?
    # List of features with a missing value ratio above 0.6
    st.write(missing_values_ratios(df))

# There are no missing values in this dataset

# Check for duplicate rows
# Count the number of duplicate rows
num_duplicate_rows = df.duplicated().sum()

if st.sidebar.checkbox("Duplicate rows"):
    st.subheader('Number of duplicate rows')
    st.write("%d rows are duplicates (that's a lot!)" % (num_duplicate_rows))

# Drop duplicates
# There are a lot of duplicate rows, so keeping them may not be a good idea
df = df.drop_duplicates()

# Check for class imbalance
if st.sidebar.checkbox('Class imbalance'):
    st.subheader('Class imbalance')
    counts = df['success'].value_counts()
    
    fig, ax = plt.subplots(figsize=(6.4, 2.4))
    sns.barplot(x=counts.index, y=counts.values, ax=ax)
    ax.set_xticklabels(['No', 'Yes'])
    ax.set_xlabel('Subscribed to term deposit')
    ax.set_ylabel('Number of clients')
    ax.set_title('Class imbalance')
    st.pyplot(fig)

    subscribers = counts[1]
    non_subscribers = counts[0]
    st.write('Degree of imbalance: %.1f to 1 non-subscribers to subscribers' % 
        (non_subscribers/subscribers))

# MODELING
# Checklist:
# Create a pipeline for pre-processing features
# Create a pipeline for training the model

# Create a pipeline for pre-processing features
# This should also take care of missing values (here, there are none)
def pre_processor(numerical_features, categorical_features):
    # Pipeline for pre-processing numeric features
    # Scale all values to zero mean and unit variance (many algorithms assume this)
    numerical_transformer = Pipeline(        
        steps = [('scaler', StandardScaler())])
        # If we had missing values, we could use SimpleImputer here
        # steps = [('imputer', SimpleImputer(strategy='constant', fill_value=0)),
        #     ('scaler', StandardScaler())])

    # Pipeline for pre-processing categorical features
    # One-hot encode the values
    categorical_transformer = Pipeline(
        steps = [('onehot', OneHotEncoder(handle_unknown='ignore'))])
        # If we had missing values, we could use SimpleImputer here
        # steps = [('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        #     ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    # Combine the two pipelines into one
    preprocessor = ColumnTransformer(
        transformers = [('num', numerical_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)])
    # Also return a handle to the one-hot encoder (needed for feature importance)
    return preprocessor

# Create a pipeline for training the model
preprocessor = pre_processor(numerical_features, categorical_features)
type_of_classifier = st.sidebar.radio("Select type of classifier", 
    ("Decision Tree", "Logistic Regression", "Gradient Boosting", "Neural Network"))
if type_of_classifier == "Decision Tree":
    classifier = DecisionTreeClassifier(max_depth=3, class_weight='balanced')
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
# Split the data into 80% training and 20% testing
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True, stratify=y, random_state=42)

# In the bank marketing dataset, however, samples are ordered by time (Moro et al., 2014). 
# Therefore, we should use a time-split, instead (set shuffle=False)
# As suggested by Moro et al., we use the first 4 years for training and the last year for testing
# The last year comprises 2058 samples (which is 5% of the total number of samples)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=2058, shuffle=False)

# Identify the most suitable performance metrics for evaluating the model
# If the classes are balanced, accuracy is a good metric
# Otherwise, most of the time, we would use the F1 score which balances precision and recall
# However, there may be better metrics for a specific problem

# Choose a way to deal with imbalanced data
# General strategies:
# We can use class weights to balance the classes
# We can also oversample the minority class or undersample the majority class
# Here, we will use class weights (class_weight='balanced')
# Since the samples are ordered by time, but we don't have additional infomation on
# when the samples were collected, we cannot use oversampling (eg for each day)

# Use k-fold cross-validation to evaluate the model
# cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
# scores = cross_validate(model, X_train, y_train, cv=cv, n_jobs=-1,
#   scoring=['accuracy', 'roc_auc', 'precision', 'recall', 'f1'])

# Create cross-validation indices for time series data
# We will use a rolling window of length W
# offset is the index of the first training sample
# L is the length of the test set
# K is the number of predictions made each update
def cv_windows(X, W, L, K):
    offset = compute_offset(X, W, L)
    folds = []
    n_splits = L // K + 1
    for i in range(n_splits):
        start = offset + i * K
        train_indices = list(range(start, start + W))
        test_indices = list(range(start + W, start + W + K))
        folds.append((train_indices, test_indices))
    last_fold = folds.pop()
    if last_fold[1][-1] > X.shape[0]:
        last_fold = (last_fold[0], list(range(last_fold[1][0], X.shape[0])))
    folds.append(last_fold)
    return folds

# First fold should start at len(X) - W - L
def compute_offset(X, W, L):
    offset = X.shape[0] - W - L
    return offset

# Use a rolling window to simulate a real-world scenario
# Choices of L, K and W based on Moro et al. (2014)
L = 2058
W = 20000
K = 10
cv = cv_windows(X, W, L, K)

if st.sidebar.checkbox("Show model performance (cross validation)"):
    st.subheader('Model performance (cross validation)')
    scores = cross_validate(model, X, y, cv=cv, n_jobs=-1,
        scoring=['accuracy', 'roc_auc', 'precision', 'recall', 'f1'])
    # Performance scores for each fold
    st.write("Scores for each fold (only positive class):")
    df_scores = pd.DataFrame(scores).transpose()
    df_scores['mean'] = df_scores.mean(axis=1)
    st.dataframe(df_scores)

# Fit and evaluate the model against the test dataset
# This model can be used to make predictions on unseen data
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

if st.sidebar.checkbox('Show model performance', value=True):
    st.subheader('Model performance')
    st.write(f"The table shows the performance of the {type_of_classifier} classifier on the test data.")
    # Scores from applying the model to the test dataset
    score = metrics.classification_report(y_test, y_pred, output_dict=True)
    # Add AUC score to the report
    score['auc'] = metrics.roc_auc_score(y_test, y_pred)
    score = pd.DataFrame(score).transpose()
    st.write("Scores from applying the model to the test dataset:")
    st.write(score)

if st.sidebar.checkbox('Show confusion matrix'):
    st.subheader('Confusion matrix')
    # Confusion matrix
    conf_matrix = metrics.confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6.4, 4.8))
    sns.heatmap(conf_matrix, annot=True, fmt='d', ax=ax, cmap=plt.cm.Greens)
    ax.set_xlabel('Predicted')
    ax.set_ylabel('Actual')
    ax.set_title('Confusion matrix')
    ax.xaxis.set_ticklabels(['No', 'Yes'])
    ax.yaxis.set_ticklabels(['No', 'Yes'])
    st.pyplot(fig)

# Get feature names
# Optional: setting verbose_feature_names_out to False will remove the name of the transformer
model.named_steps['preprocessor'].verbose_feature_names_out=False
feature_names = model.named_steps['preprocessor'].get_feature_names_out()

# Draw a decision tree using sklearn
if st.sidebar.checkbox('Show decision tree'):
    if type_of_classifier == "Decision Tree":
        st.subheader('Decision tree')
        # Draw a decision tree using sklearn
        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        plot_tree(model.named_steps['classifier'], feature_names=feature_names, class_names=['No', 'Yes'], filled=True, ax=ax)
        st.pyplot(fig)
        
if st.sidebar.checkbox('Show feature importance'):
    st.subheader('Feature importance')
    if type_of_classifier == 'Logistic Regression':
        st.write("Feature importance not supported by logistic regression")
    else:
        # Get feature importance from the model
        feature_importance = model.named_steps['classifier'].feature_importances_
        # Create a dataframe with the feature names and their importance
        feature_importance = pd.DataFrame({'feature': feature_names, 'importance': model['classifier'].feature_importances_})
        feature_importance = feature_importance.sort_values('importance', ascending=False)
        # Only include the top 10 features
        feature_importance = feature_importance.head(10)
        # Plot the feature importance as horizontal bar chart
        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        sns.barplot(x='importance', y='feature', data=feature_importance, ax=ax, color='blue')
        ax.set_xlabel('Feature importance')
        ax.set_ylabel('Feature')
        ax.set_title("Feature importance")
        st.pyplot(fig)

if st.sidebar.checkbox('Show partial dependence plots'):
    st.subheader("Partial dependence plots")
    if type_of_classifier == 'Logistic Regression' or type_of_classifier == 'Neural Network':
        st.write(f"Partial dependence plots not supported for {type_of_classifier}")
    else:
        # Get partial dependence plots
        features = ['age', 'euribor3m']
        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        # Plot partial dependence plots using PartialDependenceDisplay.from_estimator
        # https://scikit-learn.org/stable/auto_examples/miscellaneous/plot_partial_dependence_visualization_api.html
        PartialDependenceDisplay.from_estimator(model, X, features, ax=ax)
        st.pyplot(fig)

if st.sidebar.checkbox('Show surrogate model'):
    st.subheader("Surrogate model")
    if type_of_classifier == 'Neural Network':
        # Train a surrogate model on the output of the neural network
        # We will use a simple decision tree
        surrogate_model = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', DecisionTreeClassifier(max_depth=3, ccp_alpha=0.001, random_state=42))
            ])
        # Get the output of the neural network
        y_train_nn = model.predict(X_train)

        # # Get degree of confidence in the prediction
        # y_train_nn_confidence = model.predict_proba(X_train)
        # # Choose indices of predictions with confidence > 0.9
        # idx = np.where(y_train_nn_confidence[:, 1] > 0.9)[0]
        # X_train, y_train_nn = X_train[idx], y_train_nn[idx]

        # Fit the surrogate model
        surrogate_model.fit(X_train, y_train_nn)

        # Draw a decision tree using sklearn
        fig, ax = plt.subplots(figsize=(6.4, 4.8))
        plot_tree(surrogate_model.named_steps['classifier'], feature_names=feature_names, class_names=['No', 'Yes'], filled=True, ax=ax)
        st.pyplot(fig)
    else:
        st.write("Surrogate model not supported by a {}".format(type_of_classifier))
