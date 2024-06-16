import requests
import json
from sqlalchemy.orm import Session
from datetime import datetime

from app.config import Config
from app.exception import ValidationError
from database.transaction import transaction
from database.model import Admin, Campaign, Recipient



class CampaignController:
    def __init__(self) -> None:
        pass

    
    def validate(self, payload):
        for value in payload.__dict__.values():
            if not value:
                raise ValidationError("Please fill all fields")


    def send_sms(self, payload) -> tuple[int, str]:
        recipients = set(payload.recipients)   # remove duplicate numbers
        
        body = json.dumps({
        "messages": [
            {
            "channel": "sms",
            "recipients": list(recipients),
            "content": payload.content,
            "msg_type": "text",
            "data_coding": "text"
            }
        ],
        "message_globals": {
            "originator": payload.originator,
            "report_url": Config.REPORT_URL
        }
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {Config.TOKEN}'
        }

        try:
            requests.request("POST", Config.SMS_API, headers=headers, data=body)
            
            return 1, None
        except Exception as e:
            return 0, str(e.args)



    def createCampainger(self, db, payload, status, api_log) -> int:
        camp = Campaign(
            name = payload.campaignName,
            originator = payload.originator,
            content = payload.content,
            created_at = datetime.now(),
            status = status,
            log = api_log
        )
        db.add(camp)
        db.flush()

        return camp.id



    @transaction
    def index(self, db: Session, payload):
        self.validate(payload)

        status, api_log = self.send_sms(payload)

        camp_id = self.createCampainger(db, payload, status, api_log)
        recipients_list = []

        for num in payload.recipients:
            recipients_list.append(
                Recipient(
                    campaign_id = camp_id,
                    send_to = num.strip()
                )
            )
        
        db.bulk_save_objects(recipients_list)
