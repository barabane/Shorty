from os import environ
from dotenv import load_dotenv
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
            f"mysql+pymysql://{environ.get('DB_USER')}:{environ.get('DB_PASS')}@{environ.get('DB_HOST')}/{environ.get('DB_NAME')}?charset=utf8mb4",
            echo=True)
        self.metadata = BaseModel.metadata
        self.session = sessionmaker(bind=self.engine)
        self.metadata.create_all(bind=self.engine)


db = DataBase()
