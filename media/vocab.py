import warnings
warnings.filterwarnings(action='ignore')

import pandas as pd

df = pd.read_csv('naiveb/clean.csv')
from sklearn.model_selection import train_test_split
X = df.text
y = df.title
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(binary=False,max_features=3500,min_df=2,max_df=0.5) 

X_train_vect = vect.fit_transform(X)


