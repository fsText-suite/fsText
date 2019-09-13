import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import gensim.downloader as api
from scipy import spatial
from sklearn import preprocessing
import re

class cosine_classifier():

    def __init__(self):

        self.model = api.load("word2vec-google-news-300")
        self.le = preprocessing.LabelEncoder()

    def clean_line(self, line):

        clean_line = ""

        line = line.replace("’", "")
        line = line.replace("'", "")
        line = line.replace("-", " ")  # replace hyphens with spaces
        line = line.replace("\t", " ")
        line = line.replace("\n", " ")
        line = line.lower()

        for char in line:
            if char in "qwertyuiopasdfghjklzxcvbnm ":
                clean_line += char
            else:
                clean_line += " "

        clean_line = re.sub(" +", " ", clean_line)  # delete extra spaces
        if clean_line[0] == " ":
            clean_line = clean_line[1:]
        return clean_line

    def preprocess(self, txt):

        txt = txt.apply(lambda x: self.clean_line(x))

        return txt

    def filter_text(self, raw_text):

        """ 
		Excluding unknown words and get corresponding token
		"""
        raw_text = raw_text.split()

        return list(filter(lambda x: x in self.model.vocab, raw_text))

    def transform_text(self, txt):

        tokens = self.filter_text(txt)

        if not tokens:
            return np.zeros(self.model.vector_size)

        text_vector = np.mean(self.model[tokens], axis=0)

        return np.array(text_vector)

    def label_encoder(self, y_train):
        return self.le.fit_transform(y_train)

    def fit(self, X_train, y_train):

        X_train = self.preprocess(X_train)
        X_train = X_train.apply(lambda x : self.transform_text(x))

        print(X_train)
        
        y_train = self.label_encoder(y_train)

        X_train_mean = pd.DataFrame(X_train).apply(pd.Series)

        print(X_train_mean)

        self.classes = np.unique(y_train)

        mean_embedding = {}
        for cl in self.classes :
            print(np.mean((X_train_mean[y_train == cl]), axis=0))
            mean_embedding[cl] = np.mean((X_train_mean[y_train == cl]), axis=0)

        self.embedding_fit = mean_embedding

    def classify_txt(self, txt):

        best_dist = 1
        best_label = -1

        for cl in self.classes :

            dist = spatial.distance.cosine(
                self.transform_text(txt), self.embedding_fit[cl]
            )

            print(dist)

            if dist <= best_dist:
                best_dist = dist
                best_label = cl

        return best_label

    def predict(self, X_test):

        X_test = self.preprocess(X_test)
        y_pred = np.array([self.classify_txt(t) for t in X_test])
        y_pred = self.le.inverse_transform(y_pred)

        return y_pred
