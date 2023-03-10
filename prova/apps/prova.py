import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

from sklearn.datasets import load_iris

from prova1.config.AppConfig import DATAPATH

dataframe = pd.read_csv(DATAPATH, header=None)

dataset = dataframe.values

