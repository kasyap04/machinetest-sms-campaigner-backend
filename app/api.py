from fastapi import APIRouter

from controller.campaign import CampaignController
from app.schema import CampaignerSchema
from app.exception import ValidationError


router = APIRouter()

@router.get("/")
def root():
    return "Welcome to SMS Campaigner"



@router.post("/create-campaign")
async def createCampaigner(items : CampaignerSchema):
    try:
        controller = CampaignController()
        controller.index(items)

        return {
            'status' : True,
            'msg' : 'SMS send successfully'
        }
    except ValidationError as e:
        return {
            'status' : False,
            'msg' : e.args[0]
        }
    except Exception as e:
        print(e.args)
        return {
            'status' : False,
            'msg': "Error occured"
        }
