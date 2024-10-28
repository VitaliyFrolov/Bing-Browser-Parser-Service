from fastapi import FastAPI
from views.get_search_data import router


app = FastAPI()

app.include_router(router)