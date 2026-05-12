import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

# Import models
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# Oter inports
import os

# Directory Listing
cwd = os.path.dirname(__file__)
root_dir = os.path.dirname(os.path.dirname(cwd))
dataset_dir = os.path.join(root_dir, "datasets/")

# Load dataset
heart_data = pd.read_clipboard(os.path.join(dataset_dir, "heart.csv"))

# Separate out the features and labels
X = heart_data.drop(axis=1, columns='target')
Y = heart_data['target']

# Split the data

