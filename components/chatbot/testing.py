import nltk, random, json, pickle
nltk.download('punkt');nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer as WNL
from nltk.tokenize import word_tokenize
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.feature_extraction.text import CountVectorizer as CV
lemmatizer  = WNL()
context = {}
class Testing:
    def __init__(self):
        self.intents = json.load(open('intents.json').read())
        data = pickle.load(open("training_data","rb"))
        self.words = data['words']
        self.classes = data['classes']
        self.model = load_model('chatbot_model.h5')
        self.ERROR_THRESHOLD = 0.5
        self.ignore_words = list("!@#$%^&*?")
    def clean_up_sentence(self,sentence):
        sentence_words=word_tokenize(sentence.lower())
        sentence_words=list(map(lemmatizer.lemmatize,sentence_words))
        sentence_words=list(filter(lambda x:x not in 
        self.ignore_words,sentence_words))
        return set(sentence_words)
    def wordvector(self,sentence):
        cv = CV(tokenizer=lambda txt: txt.split())
        sentence_words=' '.join(self.clean_up_sentence(sentence))
        words=' '.join(self.words)
        vectorize=cv.fit([words])
        word_vector=vectorize.transform([sentence_words]).toarray().tolist()[0]
        return(np.array(word_vector))
    def classify(self,sentence):
        results=self.model.predict(np.array([self.wordvector(sentence)]))[0]
        results = list(map(lambda x: [x[0],x[1]], enumerate(results)))
        results = list(filter(lambda x: x[1]>self.ERROR_THRESHOLD ,results))
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for i in results:
            return_list.append((self.classes[i[0]],str(i[1])))
        return return_list
    def response(self,sentence,userID='TechVidvan'):
        results=self.results(sentence,userID)
        print(sentence,results)
        ans=""
        if results:
            while results:
                for i in self.intents['intents']:
                    if i['tag'] == results[0][0]:
                        if 'set' in i and not 'filter' in i:
                            context[userID] = i['set']
                        if not 'filter' in i:
                            ans=random.choice(i['responses'])
                        if userID in context and 'filter' in i and i['filter']==context[userID]:
                            if 'set' in i:
                                context[userID] = i['set']
                                ans=random.choice(i['responses'])
        results.pop(0)
        return ans if ans!="" else "Sorry ! I am still Learning.\nYou can train me by providing more datas."