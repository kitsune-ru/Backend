from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances


def determine_k(embeddings, k_min):
    clusters = [x for x in range(2, k_min * 3)]
    metrics = []
    for i in clusters:
        metrics.append((KMeans(n_clusters=i).fit(embeddings)).inertia_)
    k = elbow(k_min, clusters, metrics)
    return k


def elbow(k_min, clusters, metrics):
    score = []

    for i in range(k_min, clusters[-3]):
        y1 = np.array(metrics)[:i + 1]
        y2 = np.array(metrics)[i:]

        df1 = pd.DataFrame({'x': clusters[:i + 1], 'y': y1})
        df2 = pd.DataFrame({'x': clusters[i:], 'y': y2})

        reg1 = LinearRegression().fit(np.asarray(df1.x).reshape(-1, 1), df1.y)
        reg2 = LinearRegression().fit(np.asarray(df2.x).reshape(-1, 1), df2.y)

        y1_pred = reg1.predict(np.asarray(df1.x).reshape(-1, 1))
        y2_pred = reg2.predict(np.asarray(df2.x).reshape(-1, 1))

        score.append(mean_squared_error(y1, y1_pred) + mean_squared_error(y2, y2_pred))

    return np.argmin(score) + k_min


def create_clusters(seed, word_vectors, k_min):

    opt_cluster = determine_k(word_vectors.vectors, k_min)

    cluster = KMeans(n_clusters=opt_cluster, random_state=seed).fit(word_vectors.vectors)

    data = pd.DataFrame()
    data['text'] = word_vectors.key_to_index
    data['label'] = cluster.labels_
    l = []
    for i in word_vectors.vectors:
        l.append(i)
    data['embedding'] = l

    cluster_center = pd.DataFrame()
    embeddings = []
    for i in cluster.cluster_centers_:
        embeddings.append(list(i))
    cluster_center['embeddings'] = embeddings


    "Генерация названий кластеров"

    cluster_center['tags'] = create_tags_of_clusters(data, cluster.cluster_centers_, opt_cluster)



    return data, cluster_center


def create_tags_of_clusters(data, cluster_cent, count_of_cluster):
    top_texts_list = []
    for i in range(0, count_of_cluster):
        cluster = data[data['label'] == i]
        embeddings = list(cluster['embedding'])
        texts = list(cluster['text'])
        distances = [euclidean_distances(cluster_cent[0].reshape(1, -1), e.reshape(1, -1))[0][0] for e in embeddings]
        scores = list(zip(texts, distances))
        top_3 = sorted(scores, key=lambda x: x[1])[:5]
        top_texts = list(zip(*top_3))[0]
        top_texts_list.append(top_texts)

    return top_texts_list