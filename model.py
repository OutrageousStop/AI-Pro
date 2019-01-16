import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras import utils
import nltk
from nltk.corpus import stopwords

data_encoding = 'ISO-8859-1'
data_labels = ['target', 'ids', 'date', 'flag', 'user', 'text']

data = pd.read_csv('./data/dataset.csv', encoding = data_encoding, names = data_labels)

result_map = {0: "Negative", 2: "Neutral", 4: "Positive"}

print(data.head())