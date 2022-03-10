# Backend

## Installation

```shell
git clone https://github.com/kitsune-ru/backend.git && cd backend
python3 -m venv ./venv && source ./venv/bin/activate
pip install -r ./requirements.txt
uvicorn main:app --reload

docker-compose up --build for database set up
db_user: root
db_password: root
db: kitsune_db
```

## Usage example

```
http://localhost:8000/ for web
http://localhost:8000/docs#/ for swagger documents
```
