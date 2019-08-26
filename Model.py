import pickle
import re
from string import punctuation
from konlpy.tag import Okt
from functools import reduce
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression



class W2V_LR():
    def __init__(self):
        with open("./tmp_model1", "rb") as fp:  #
            self.model = pickle.load(fp)
        with open("./w2v_model52", "rb") as fp:  #
            self.w2v_model = pickle.load(fp)
        self.okt = Okt()

    def predict_article(self, news):
        data = [_[0] for _ in self.okt.pos(news) if _[1] == "Noun"]
        predicted = self.model.predict_proba(self.w2v_corpus(data))

        return predicted

    def predict_sentences(self, news):
        sentences = news.split(". ")
        data = []
        for s in sentences:
            temp = [_[0] for _ in self.okt.pos(s) if _[1] == "Noun"]
            if temp:
                data.append(temp)
        predicted = self.model.predict_proba(self.w2v_corpus(data))
        return [sentences[i] for i in predicted if predicted[i][0] < 0.3 or predicted[i][0] > 0.7]


    def w2v_corpus(self, corpus):
        return [reduce(lambda x, y: x + y, [self.w2v_model[word] for word in doc if word in self.w2v_model]
                       , np.zeros(100)) for doc in corpus]