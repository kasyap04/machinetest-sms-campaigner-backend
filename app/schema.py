from pydantic import BaseModel


class AuthSchema(BaseModel):
    username : str
    password : str


class CampaignerSchema(BaseModel):
    campaignName : str
    originator : str
    recipients : list
    content : str