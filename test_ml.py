import pytest
import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")

data_path = './data/census.csv'
model_path = './model/model.pkl'

categorical_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


@pytest.fixture(name='data')
def load_data():
    """
    returns dataframe loaded from csv.
    """
    return pd.read_csv(data_path)


@pytest.fixture()
def model():
    return load_model(model_path)

def load_model(model_path):
    # Load model from path
    with open (model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def preprocess_data(df, categorical_features, label):
    # convert to dummy variable
    df_processed = pd.get_dummies(df, columns=categorical_features)
    X = df_processed.drop(label, axis=1)
    y = df_processed[label]
    return X, y

def test_data_type(data):
    #Ensures feature is DataFrame and label is Series
    train, _ = train_test_split(data, test_size = 0.20, random_state = 42)
    X, y = preprocess_data(train, categorical_features, 'salary')
    assert isinstance(X, pd.DataFrame), "Processed features is DataFrame"
    assert isinstance(y, pd.Series), "Processed labels is Series"

def test_model_type(model):
    assert isinstance(model, RandomForestClassifier), "Model is RandomForestClassifier"

def test_not_empty(data):
    # Ensures dataframe and not empty
    assert isinstance(data, pd.DataFrame), "data is a dataframe"
    assert not data.empty, "dataframe not empty"
    