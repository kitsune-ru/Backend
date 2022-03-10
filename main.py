import datetime
import time
import pandas

from fastapi import FastAPI
import uvicorn
from db.base import init_sessionmaker, session_scope, database
from endpoint import users, auth, services
from ML import start as ML_start



app = FastAPI(title="Kitsune")
init_sessionmaker()
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(services.router, prefix="/services", tags=["services"])


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
    print(Answ[0])
    print(Answ[1])
    print(Answ[2])
#    with session_scope() as session:
#        session.execute('''INSERT INTO ML_regular_entries (text, embedding, label)
#                               VALUES (:text,:embedding,:label)''',
#                        {
#                            'text': Answ[0]["text"].tolist(), 'embedding': Answ[0]["embedding"].tolist(), 'label': Answ[0]["label"].tolist(),
#                        })
#        session.execute('''INSERT INTO ML_cluster_center (tags, density, embedding, distantion)
#                                       VALUES (:tags,:density,:embedding,:distantion)''',
#                        {
#                            'tags': Answ[1]["tags"].tolist(), 'density': Answ[1]["density"].tolist(), 'embedding': Answ[1]["embedding"].tolist(), 'distantion': Answ[1]["distantion"].tolist(),
#                        })
#
#        session.execute('''INSERT INTO ML_emotion (name, embedding)
#                                       VALUES (:name,:embedding)''',
#                        {
#                            'text': Answ[2]["name"].tolist(), 'embedding': Answ[2]["embedding"].tolist(),
#                        })

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()