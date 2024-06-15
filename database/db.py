from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.model import Base

SQLALCHEMY_DATABASE_URL = f"postgresql://vishnu:vishnu@localhost/sms_campaigner"

engine      = create_engine(SQLALCHEMY_DATABASE_URL)
BaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)