from pydantic import BaseModel


class CampaignerSchema(BaseModel):
    name : str
    originator : str
    recipients : list[str]
    content : str