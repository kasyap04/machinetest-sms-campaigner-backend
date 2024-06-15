from fastapi import FastAPI

from app.schema import CampaignerSchema
from controller.base import BaseController

app = FastAPI()


@app.get("/")
def root():
    BaseController().auth()
    return {'s' :"hello"}


@app.post("/create-campaign")
def createCampaigner(items = CampaignerSchema):
    controller = BaseController()
    controller.createCamp()