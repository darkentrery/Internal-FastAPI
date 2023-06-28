from fastapi import FastAPI
from pydantic import BaseModel
from env_fastapi.settings import settings


app = FastAPI()


class Status(BaseModel):
    status: str = "ok"


@app.get(settings.main_url)
async def status():
    return Status()
