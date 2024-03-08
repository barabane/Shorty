from models.BaseModel import BaseModel, uuid_pk, time_now
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, Text
from sqlalchemy.dialects.mysql import LONGTEXT


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[uuid_pk]
    email: Mapped[str] = mapped_column(VARCHAR(100), unique=True)
    password: Mapped[str] = mapped_column(LONGTEXT)
    reg_at: Mapped[time_now]
