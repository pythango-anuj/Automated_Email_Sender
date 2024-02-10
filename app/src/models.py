from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()

# User model for authentication
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=True)
    password = Column(String, nullable=False)

    campaigns = relationship('Campaign', back_populates='user')
    

# Campaign model
class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    send_from = Column(String, nullable=False)
    send_to = Column(String, nullable=False) 
    bcc = Column(String)  
    email_body = Column(Text, nullable=False)
    schedule_time = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    num_sents_allowed = Column(Integer, nullable=False)

    # ForeignKey relationship to User
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='campaigns')
