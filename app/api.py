from fastapi import APIRouter, Response, Request

from controller.campaign import CampaignController
from controller.auth import AuthController
from app.schema import CampaignerSchema, AuthSchema
from app.exception import ValidationError


router = APIRouter()



@router.post("/auth")
async def authenticate():
    """
    Authentication is completed in middleware.
    This api will work only if the if its authenticated
    """
    return {'status': True}



@router.post("/login")
async def authenticate(response: Response, payload: AuthSchema):
    try:
        contoller = AuthController()
        status = contoller.login(payload.username, payload.password, response=response)


        if not status:
            raise ValidationError("Incorrect username or password")

        return {
            'status' : True,
            'msg' : 'loged in'
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
