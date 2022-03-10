import numpy as np
import pandas as pd
from gensim.models import Phrases
from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count

def load_the_data_xlx(path):
    data = pd.read_excel(path)
    return data


def load_the_data_csv(path):
    data = pd.read_csv(path).sort_values(by='time', ascending=False)

    return data

def word2vec_method(prepr_data, vec_dim=10, seed=42):
    model = Word2Vec(prepr_data, min_count=0, window=5, workers=cpu_count(), vector_size=vec_dim, seed=seed)
    return model

def create_emotions(Dimention,seed, Emotion):
    temp = []

    for i in Emotion['datas']:
        temp.append(i.split())

    test_model_w2v = word2vec_method(temp, vec_dim=Dimention, seed=seed)



    Emotion = pd.DataFrame()
    Emotion['datas']=list(test_model_w2v.wv.key_to_index)
    Emotion['embeddings'] = list(test_model_w2v.wv.vectors)

    return Emotion

def create_w2v(clean_text,count_of_w2v,seed,min_count,threshold):

    bigram = Phrases(clean_text, min_count=min_count, threshold=threshold)
    test_model_w2v = word2vec_method(bigram[clean_text], vec_dim=count_of_w2v, seed=seed)
    word_vectors = test_model_w2v.wv

    return word_vectors

