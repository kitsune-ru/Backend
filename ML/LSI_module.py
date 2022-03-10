import pandas as pd
from ML import preproc as pp
from gensim.models import LsiModel


def create_model(txt, number_of_topics):
    dictionary, text_term_matrix = pp.prepare_corp(txt)
    lsamodel = LsiModel(corpus=text_term_matrix, num_topics=number_of_topics, id2word=dictionary)
    return lsamodel


def return_data_frame_of_themes(clean_text):
    lsi_model = create_model(clean_text, 2)

    Themes = []
    scores = []
    for c in range(len(lsi_model.id2word.id2token)):
        Themes.append(lsi_model.id2word.id2token[c])
        scores.append(lsi_model.projection.u[c][0])

    Themes = pd.DataFrame(data=[Themes, scores])
    Themes = Themes.transpose()
    Themes.columns = ['Тема', "Оценка"]
    Themes['Оценка'] = Themes['Оценка'].astype('float')
    Themes = Themes.sort_values(by=['Оценка'], ascending=False)
    return Themes
