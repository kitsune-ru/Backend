import datetime
import time
import pandas

from fastapi import FastAPI
import uvicorn
from db.base import init_sessionmaker, session_scope, database
from endpoint import users, auth, services, ML_emotion, ML_regular_entries, ML_cluster_center
from ML import start as ML_start



app = FastAPI(title="Kitsune")
init_sessionmaker()
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(services.router, prefix="/services", tags=["services"])
app.include_router(ML_emotion.router, prefix="/ML_emotion", tags=["ML_emotion"])
app.include_router(ML_regular_entries.router, prefix="/ML_regular_entries", tags=["ML_regular_entries"])
app.include_router(ML_cluster_center.router, prefix="/ML_cluster_center", tags=["ML_cluster_center"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("startup")
async def create_ML():
    Data = [['У попа была собака', "Он ее любил", "Она съела кусок мяса",
             'Он ее убил', "В яму закопал", "На могиле написал"], ['0', '1', '3', '4', '5', '6']]
    'Нужно каким=то образом преобразовать полученное в Dataframe'
    Data = pandas.DataFrame(data=Data)
    Data = Data.transpose()
    Data.columns = ['data', 'time']

    # Emotions = services.get_all_cluster_emotion()
    Emotions = ['Не отображается', "Не прошел платеж", "РРРР!"]
    Emotions = pandas.DataFrame(data=Emotions, columns=['datas'])
    Answ = ML_start.return_sost_FA(Data, Emotions, 1)
    # print(Answ[0])
    # print(Answ[1])
    # print(Answ[2])

    '-------------------------------------------------------------'
    'Выгрузка в базу данных построчно ML_emotion, ML_regular_entries, ML_cluster_center'


    '1 - точки ML_regular_entries'

    for i in Answ[0].values.tolist():
       with session_scope() as session:
           session.execute('''INSERT INTO ML_regular_entries (text, embedding, label)
                                  VALUES (:text,:embedding,:label)''',
                           {
                               'text': str(i[0]), 'embedding': str(i[2]), 'label': int(i[1]),
                           })

    '2 - точки ML_emotion'

    for i in Answ[2].values.tolist():
        with session_scope() as session:
            session.execute('''INSERT INTO ML_emotion (name, embedding)
                                                  VALUES (:name,:embedding)''',
                                                   {
                                                       'name': str(i[0]), 'embedding': str(i[1]),
                                                   })

    '3 - точки ML_cluster_center'

    for i in Answ[1].values.tolist():
        with session_scope() as session:
            session.execute('''INSERT INTO ML_cluster_center (tags, density, embedding, distantion)
                                                  VALUES (:tags,:density,:embedding,:distantion)''',
                                   {
                                       'tags': str(i[1]), 'density': float(i[3]), 'embedding': str(i[0]), 'distantion': str(i[2]),
                                   })


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()