import nltk, random, json, pickle
nltk.download('punkt');nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import flatten
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation,Dropout 
from tensorflow.keras.optimizers import SGD
lemmatizer = WordNetLemmatizer
class Training:
    def __init__(self):
        df = open('intents.json').read()
        self.intents = json.loads(df)['intents']
        self.ignore_words = list("!@#$%^&*?")
        self.process_data()