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
            f"mysql+pymysql://{environ.get('DB_USER')}:{environ.get('DB_PASS')}@{environ.get('DB_HOST')}/{environ.get('DB_NAME')}?charset=utf8mb4")
        self.metadata = BaseModel.metadata
        self.session = sessionmaker(bind=self.engine)()
        self.metadata.create_all(bind=self.engine)
        # self.metadata.drop_all(bind=self.engine)

    def get_user_by_email(self, email: str):
        return self.session.execute(select(User).where(User.email == email))

    def register_user(self, email: str, password: str):
        is_exists = self.get_user_by_email(email).scalar()

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
        return f"https://shrt.ru/{str(uuid.uuid4())[0:6]}"

    def create_url(self, user_id: str, full_url: str):
        new_url = URL(
            user_id=user_id,
            full_path=full_url,
            short_path=self._generate_short_url()
        )

        self.session.add(new_url)
        self.session.commit()

        return new_url

    def get_user_urls(self, user_id: str):
        return self.session.scalars(select(URL).where(URL.user_id == user_id)).all()

    def get_url(self, url_id: str):
        return self.session.get(URL, url_id)

    def get_url_stats(self, url_id: str):
        return self.session.scalars(select(Visit).where(Visit.url_id == url_id)).all()


db = DataBase()
db.get_url_stats('9f0019a5-47cb-4594-851e-e673e66651e0')
