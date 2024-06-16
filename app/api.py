from fastapi import APIRouter, Response, Request

from controller.campaign import CampaignController
from controller.auth import AuthController
from app.schema import CampaignerSchema, AuthSchema
from app.exception import ValidationError
from app.config import Config


router = APIRouter()



@router.post("/auth")
async def authenticate(response: Response, request: Request):
    """
    Authentication is completed in middleware and the result pass through state
    """
    if not request.state.verifyToken:
        response.delete_cookie(Config.AUTH_SESSION_KEY)

    return {'status': request.state.verifyToken}



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


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(Config.AUTH_SESSION_KEY)

    return {'status': True}



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
