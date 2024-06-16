from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DatabaseConfig
from database.model import Base



SQLALCHEMY_DATABASE_URL = f"postgresql://{DatabaseConfig.DB_USER}:{DatabaseConfig.DB_PASSWORD}@{DatabaseConfig.DB_HOST}:{DatabaseConfig.DB_PORT}/{DatabaseConfig.DB_NAME}"

engine      = create_engine(SQLALCHEMY_DATABASE_URL)
BaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)