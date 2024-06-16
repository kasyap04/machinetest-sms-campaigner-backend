from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, TIMESTAMP, Integer, String, Column, text
from sqlalchemy.dialects.mysql import BIGINT


Base = declarative_base()


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(BIGINT, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(255), nullable=False)



class Campaign(Base):
    __tablename__ = 'campaign'

    id = Column(BIGINT, primary_key=True)
    name = Column(String(50), nullable=False)
    originator = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    status = Column(Integer)
    log = Column(String(800), nullable=True)



class Recipient(Base):
    __tablename__ = 'recipient'

    id = Column(BIGINT, primary_key=True)
    campaign_id = Column(ForeignKey('campaign.id', ondelete=u'CASCADE'), index=True)
    send_to = Column(String(15), nullable=False)
