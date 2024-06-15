from pydantic import BaseModel


class CampaignerSchema(BaseModel):
    campaignName : str
    originator : str
    recipients : list
    content : str