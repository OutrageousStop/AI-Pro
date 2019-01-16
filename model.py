import pandas as pd
from keras.preprocessing.text import text_to_word_sequence

data_encoding = 'ISO-8859-1'
data_labels = ['target', 'ids', 'date', 'flag', 'user', 'text']

data = pd.read_csv('./data/dataset.csv', encoding = data_encoding, names = data_labels)

print(data.head())
