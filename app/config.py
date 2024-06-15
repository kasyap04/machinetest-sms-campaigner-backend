import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG : bool = os.getenv('DEBUG', 'TRUE') == 'TRUE'
    FRONTEND_URL : str = os.getenv('FRONTEND_URL')

    SMS_API : str       = os.getenv('SMS_API')
    TOKEN : str         = os.getenv('TOKEN')
    REPORT_URL : str    = os.getenv('REPORT_URL')


class DatabaseConfig:
    DB_NAME : str       = os.getenv('DB_NAME')
    DB_USER : str       = os.getenv('DB_USER')
    DB_PASSWORD : str   = os.getenv('DB_PASSWORD')
    DB_HOST : str       = os.getenv('DB_HOST')
    DB_PORT : int       = int(os.getenv('DB_PORT', 5432))