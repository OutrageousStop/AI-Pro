import tensorflow as tf
import gensim
import pickle
import time
import re
import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from keras.preprocessing.sequence import pad_sequences
from  nltk.stem import SnowballStemmer

w2v_model = gensim.models.Word2Vec.load("model.w2v")

with open('tokenizer.pkl', 'rb') as loader:
    tokenizer = pickle.load(loader)

with open('encoder.pkl', 'rb') as loader:
    encoder = pickle.load(loader)

model = tf.keras.models.load_model('model.h5')

POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)
SEQUENCE_LENGTH = 300

def decode_sentiment(score, include_neutral=True):
    if include_neutral:        
        label = NEUTRAL
        if score <= SENTIMENT_THRESHOLDS[0]:
            label = NEGATIVE
        elif score >= SENTIMENT_THRESHOLDS[1]:
            label = POSITIVE

        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE

def predict(text, include_neutral=True):
    start_at = time.time()
    # Tokenize text
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=SEQUENCE_LENGTH)
    # Predict
    score = model.predict([x_test])[0]
    # Decode sentiment
    label = decode_sentiment(score, include_neutral=include_neutral)

    #return {"label": label, "score": float(score), "elapsed_time": time.time()-start_at}  
    return {"label": label, "score": float(score)}  