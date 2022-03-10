from starlette.config import Config

config = Config(".env")

ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("EE_SECRET_KEY", cast=str, default="b122bc2b2410d2bb017cbfad58eecebdd9d7ecdbdfe0f50d8562cb7d540a0bfc")
