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
    def process_data(self):
        self.pattern = list(map(lambda x:x["patterns"], self.intents))
        self.words = list(map(word_tokenize, flatten(self.pattern)))
        self.classes = flatten([x["tag"]]*len(y) for x, y in zip(self.intents, self.pattern))
        self.words=list(map(str.lower,flatten(self.words)))
        self.words=list(filter(lambda x:x not in self.ignore_words,self.words))
        self.words=list(map(lemmatizer.lemmatize,self.words))
        self.words=sorted(list(set(self.words)))
        self.classes=sorted(list(set(self.classes)))
    def train_data(self):
        cv = CountVectorizer(tokenizer=lambda txt:txt.split(),analyzer="word",stop_words=None)
        training = []
        for doc in self.documents:
            pattern_words=list(map(str.lower,doc[0]))
            pattern_words=' '.join(list(map(lemmatizer.lemmatize,pattern_words)))
            vectorize=cv.fit([' '.join(self.words)])
            word_vector=vectorize.transform([pattern_words]).toarray().tolist()[0]
            output_row=[0]*len(self.classes)
            output_row[self.classes.index(doc[1])]=1
            cvop=cv.fit([' '.join(self.classes)])
            out_p=cvop.transform([doc[1]]).toarray().tolist()[0]
            training.append([word_vector,output_row])
            random.shuffle(training)
            training=np.array(training,dtype=object)
            train_x=list(training[:,0]) #patterns
            train_y=list(training[:,1]) #classes
            return train_x,train_y
    def build(self):
        train_x, train_y = self.train_data()
        model = Sequential()
        model.add(Dense(128,input_shape=(len(train_x[0]),),activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(64,activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(len(train_y[0]),activation='softmax'))
        sgd = SGD(lr=1e-2,decay=1e-6,momentum=0.9,nesterov=True)
        model.compile(loss='categorical_crossentropy',
        optimizer = sgd, metrics=['accuracy'])
        hist = model.fit(np.array(train_x),np.array(train_y),
        epochs=200,batch_size=10,verbose=1)