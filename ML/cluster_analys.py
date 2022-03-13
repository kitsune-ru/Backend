import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


def return_count_of_elem(data_str):
    return data_str.value_counts()

def return_rasst(cluster_center_em, Emotion):
    All_dist = []
    for i in cluster_center_em:
        dist = []
        i = np.array(i)
        for j in Emotion['embeddings']:
            d = euclidean_distances(i.reshape(1, -1), np.array(j).reshape(1, -1))
            d = d[0][0]
            dist.append(d)
        dist1 = sorted(list(zip(Emotion['datas'], dist)), key=lambda x: x[1])
        All_dist.append(dist1)
    return All_dist

def return_density(center_coord, data):
    Denst=[]
    for i in range(len(center_coord)):
        temp = []
        for j in range(len(data['embedding'])):
            if (data['label'][j]==i):
                temp.append(euclidean_distances(np.array(data['embedding'][j]).reshape(1, -1), np.array(center_coord[i]).reshape(1, -1))[0][0])

        Denst.append(1/float(sum(temp)/len(temp)))

    return Denst
def return_claster_center(cluster_center,Data, Emotion):
    'Кластерный анализ:'
    "1) Количество объектов в каждом кластере"
    "2) Расстояние от центра каждого кластера до каждой из эмоций"
    "3) Кучность кластера"

    '1 - Кол-во объектов в каждом кластере'
    claster_elements_counts = return_count_of_elem(Data['label'])

    '2 - Расстояние'
    cluster_center['distantion'] = return_rasst(cluster_center['embeddings'], Emotion)

    '3 - Кучность'
    cluster_center['density'] = return_density(cluster_center['embeddings'], Data)

    return claster_elements_counts, cluster_center

def return_FA_down(porog, dens_list):
    for i in dens_list:
        if i>=porog:
            return True
        else:
            return False