from fastapi import FastAPI
from . import models, database, routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/health")
def healthcheck():
    return {"status": "ok"}

app.include_router(routes.router)
