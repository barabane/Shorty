import uuid
from os import environ

from dotenv import load_dotenv
from sqlalchemy import select
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash

from models.BaseModel import BaseModel
from models.URL import URL
from models.User import User
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
            f"mysql+pymysql://{environ.get('DB_USER')}:{environ.get('DB_PASS')}@{environ.get('DB_HOST')}:"
            f"{environ.get('DB_PORT')}/{environ.get('DB_NAME')}?charset=utf8mb4")
        self.metadata = BaseModel.metadata
        self.session = sessionmaker(bind=self.engine)()
        self.metadata.create_all(bind=self.engine)

    def get_user_by_email(self, email: str):
        return self.session.scalar(select(User).where(User.email == email))

    def get_user_by_id(self, user_id):
        return self.session.get(User, user_id)

    def register_user(self, email: str, password: str):
        is_exists = self.get_user_by_email(email)

        if is_exists:
            return False

        new_user = User(
            email=email,
            password=generate_password_hash(password=password, salt_length=2)
        )

        self.session.add(new_user)
        self.session.commit()

        return new_user

    @staticmethod
    def _generate_short_url():
        return f"{environ.get('DOMEN')}/fp{str(uuid.uuid4())[0:4]}"

    def create_url(self, user_id: str, full_url: str):
        new_url = URL(
            user_id=user_id,
            full_path=full_url,
            short_path=self._generate_short_url()
        )

        self.session.add(new_url)
        self.session.commit()

        return new_url

    def delete_url(self, url_id: int):
        self.session.delete(self.session.get(URL, url_id))
        self.session.commit()

    def get_user_urls(self, user_id: str):
        return self.session.scalars(select(URL).where(URL.user_id == user_id)).all()

    def get_user_url(self, user_id: str, url_id: int):
        return self.session.scalar(select(URL).where(URL.id == url_id).where(URL.user_id == user_id))

    def get_url(self, url_id: str):
        return self.session.get(URL, url_id)

    def get_url_by_path(self, short_path: str):
        return self.session.scalar(select(URL).where(URL.short_path == short_path))

    def get_url_stats(self, url_id: str):
        return self.session.scalars(select(Visit).where(Visit.url_id == url_id)).all()

    def add_visit(self, url_id: str, visit_ip: str):
        self.session.add(Visit(
            url_id=url_id,
            visit_ip=visit_ip
        ))
        self.session.commit()


db = DataBase()
