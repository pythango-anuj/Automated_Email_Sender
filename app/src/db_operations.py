from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from .models import Base, User
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Create Sqlite Engine
engine = create_engine(os.getenv("DB_URL"))
Session = sessionmaker(bind=engine)


# Create Database
def create_or_update_db():
    Base.metadata.create_all(bind=engine)


# Function to add a new user
def add_user(session, username, firstname, lastname, password):
    new_user = User(username=username, firstname=firstname, lastname=lastname, password=password)
    session.add(new_user)
    try:
        session.commit()
        print(f"Added new user: {username} ({firstname} {lastname})")
    except IntegrityError as e:
        session.rollback()
        print(f"Error: {e}")
        

# Function to obtain the user
def get_login_user(session, username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    return user
