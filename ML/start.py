from ML import vectorisation as vect
from ML import clasterisation as cl
from ML import cluster_analys as ca
from ML import preproc as pp
from ML import graph as grph
from ML import LSI_module as lsi


def return_standart_input_params():
    "Размерность векторов w2v"
    count_of_w2v = 2
    "Стартовый параметр для фиксации рандомных значений алгоритмов кластеризации"
    seed = 42
    "Минимальное кол-во кластеров, сильно влияет на полученный результат"
    k_min = 4
    'Тип преобразования текстуальных переменных: TRUE - по словам, FALSE - по записям в БД'
    otdelnie_slova = True
    'Пороговое значение для формирования w2v'
    threshold = 5
    'Минимально допустимая длина биграмм для формирования вектора w2v'
    min_count = 1

    'Порог кучности, при котором принимается решение о упавшей ФА'
    density_level = 10

    return count_of_w2v, seed, k_min, otdelnie_slova, threshold, min_count, density_level

def return_sost_FA(Data, Emotions, need_art_of_answer):
    count_of_w2v, seed, k_min, otdelnie_slova, threshold, min_count,density_level = return_standart_input_params()
    '------------------------------------------'
    'Формируем исходные данные - подгружаем свежую БД сообщений и очищаем текст'

    clean_text = pp.preproc_data(Data, otdelnie_slova=otdelnie_slova)

    '------------------------------------------'
    "СОЗДАТЬ И ОБУЧИТЬ МОДЕЛЬ LSI"
    "[!] В этой таблице содержатся все темы, соответствующие БД. Они отсортированы по убыванию."
    top_theme = lsi.return_data_frame_of_themes(clean_text)
    '--------------------------------------------------------'
    "СОЗДАТЬ И ОБУЧИТЬ МОДЕЛЬ WORD2VEC"

    'исходные данные'
    word_vectors = vect.create_w2v(clean_text, count_of_w2v, seed, min_count, threshold)

    'эмоции'
    "[!] В этой таблице содержатся эмоции и их координаты."
    Emotion = vect.create_emotions(count_of_w2v, seed, Emotions)
    '-----------------------'
    'Кластеризация'
    "[!] DATA - в таблице содержатся точки, принадлежность к кластерам и их координаты"
    "[!] cluster_center - в таблице содержатся координаты центров кластеров, их теги"
    Data, cluster_center = cl.create_clusters(seed, word_vectors, k_min)
    '-------------------------------------------'
    "Кластерный анализ"
    "[!] claster_elements_counts - подсчитано кол-во элементов в каждом кластере"
    "[!] cluster_center - [Модифицировано] в таблице содержатся координаты центров кластеров, их теги + !!!расстояния до каждой эмоции и кучность!!!"
    claster_elements_counts, cluster_center = ca.return_claster_center(cluster_center, Data, Emotion)
    '-------------------------------------------'
    if (need_art_of_answer==0):
        'Визуализация - картинка'
        art = grph.create_image(Data, cluster_center, Emotion)
        return art
    if (need_art_of_answer==1):
        'Визуализация - 3 таблицы'
        return Data, cluster_center, Emotion
    else:
        FA_down = ca.return_FA_down(density_level, cluster_center['density'])
        return FA_down


# if __name__ == '__main__':
#     Data = vect.load_the_data_csv("data.csv")
#     ans = return_sost_FA(Data, 1)
#     print('!')