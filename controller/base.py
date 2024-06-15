from sqlalchemy.orm import Session

from database.transaction import transaction
from database.model import Admin



class BaseController:
    def __init__(self) -> None:
        pass


    @transaction
    def auth(self, db : Session):
        t = db.query(Admin).all()

        print(t)




    @transaction
    def createCamp(seld, db: Session):
        ...