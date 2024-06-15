from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Index, Numeric, BigInteger, ForeignKey, func, DATETIME, TIMESTAMP, String, Column, text
from sqlalchemy.dialects.mysql import TINYINT,LONGTEXT,ENUM, VARCHAR, BIGINT


Base = declarative_base()


class Admin(Base):
    __tablename__ = 'admin'

    id = Column(BIGINT, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(255), nullable=False)



class SmsContent(Base):
    __tablename__ = 'campaign_data'

    id = Column(BIGINT, primary_key=True)
    name = Column(String(50), nullable=False)
    originator = Column(String(50), nullable=False)
    content = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))



class SmsDetails(Base):
    __tablename__ = 'sms_details'

    id = Column(BIGINT, primary_key=True)
    campaign_id = Column(ForeignKey('campaign_data.id', ondelete=u'CASCADE'), index=True)
    send_to = Column(String(15), nullable=False)
