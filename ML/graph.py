import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def return_embendings(d_emb):
    data=pd.DataFrame()
    temp = []
    for i in range(len(d_emb[0])):
        for j in range(len(d_emb)):
            temp.append(d_emb[j][i])
        data['x' + str(i)] = temp
        temp = []
    return data

def create_image(data, cl_cr, em):
    D = return_embendings(data['embedding'])
    D_C = return_embendings(cl_cr['embeddings'])
    E = return_embendings(em['embeddings'])

    pca = PCA(n_components=2)
    components = pca.fit_transform(D)
    components = pd.DataFrame(data=components, columns=["X", "Y"])
    components['Номер кластера'] = data['label'].reset_index()['label']
    components['size'] = 1
    components1 = pca.fit_transform(E)
    components1 = pd.DataFrame(data=components1, columns=["X", "Y"])
    components1['Номер кластера'] = "Центр эмоции"
    components1['size'] = 6
    components2 = pca.fit_transform(D_C)
    components2 = pd.DataFrame(data=components2, columns=["X", "Y"])
    components2['Номер кластера'] = "Центр кластера"
    components2['size'] = 6

    CMP = pd.concat([components, components1, components2], axis=0)

    plt.figure(figsize=(10, 10))

    fig = sns.scatterplot(data=CMP, x="X", y="Y", hue="Номер кластера", size="size",
                    sizes=(20, 200), legend=False)

    return fig