from fastapi import FastAPI
from views.get_search_data import router
from middleware import setup_cors


app = FastAPI()
setup_cors(app) 

app.include_router(router)