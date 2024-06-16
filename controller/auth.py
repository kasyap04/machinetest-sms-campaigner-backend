import json
import bcrypt 
from itsdangerous import URLSafeTimedSerializer
from fastapi import Response, Request
from sqlalchemy.orm import Session

from app.config import Config
from database.transaction import transaction
from database.model import Admin


"""
SECRET_KEY is random string used to serialize username and password, to store serialzed data in cookie
"""
serializer = URLSafeTimedSerializer(Config.SECRET_KEY)


class AuthController:
    def __init__(self) -> None:
        pass


    def hash_password(self, password):
        salt = bcrypt.gensalt() 
        return bcrypt.hashpw(password.encode('utf-8') , salt).decode()

    def check_password(self, hashed_pwd, password) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_pwd.encode('utf-8')) 


    def gen_session_token(self, payload: dict):
        data = json.dumps(payload)
        return serializer.dumps(data)



    def verify_token(self, token):
        try:
            data = serializer.loads(token, max_age=3600)
            return json.loads(data)
        except Exception:
            return False
    


    @transaction
    def login(self, db: Session, username, password, response: Response = None, setcookie = True) -> bool:
        hashed_pwd = db.query(Admin.password).filter(Admin.username == username).scalar()
        if not hashed_pwd:
            return False


        passworc_check = self.check_password(hashed_pwd, password)
        if passworc_check and setcookie:
            token = self.gen_session_token({ 'username':username, 'password': password})
            
            response.set_cookie(
                key=Config.AUTH_SESSION_KEY,
                value=token,
                httponly=True,
                max_age=3600,
                samesite="none",
                secure=True,
                path="/"
            )


        return passworc_check



    def common_validation(self, request: Request):
        """
        Used to authenticate in middleware
        """
        token = request.cookies.get(Config.AUTH_SESSION_KEY)
        if not token:
            return False

        verify = self.verify_token(token)
        if not verify:
            return False
        
        check_login = self.login(**verify, setcookie=False)

        return check_login
