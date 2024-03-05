from os import environ
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

from models.BaseModel import BaseModel
from models.User import User
from models.URL import URL
from models.Visit import Visit

load_dotenv()


class DataBase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataBase, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.engine = create_engine(
            f"mysql+pymysql://{environ.get('DB_USER')}:{environ.get('DB_PASS')}@{environ.get('DB_HOST')}/{environ.get('DB_NAME')}?charset=utf8mb4")
        self.metadata = BaseModel.metadata
        self.session = sessionmaker(bind=self.engine)()
        self.metadata.create_all(bind=self.engine)

    def get_user_by_email(self, email: str):
        user = self.session.execute(select(User).where(User.email == email))

        return user

    def register_user(self, email: str, password: str):
        is_exists = self.get_user_by_email(email)

        if is_exists:
            return False

        new_user = User(
            email=email,
            password=generate_password_hash(password=password, salt_length=5)
        )

        self.session.add(new_user)
        self.session.commit()

        return new_user



db = DataBase()
