from models.BaseModel import BaseModel, uuid_pk, time_now
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import VARCHAR


class User(BaseModel):
    __tablename__ = "user"

    id: Mapped[uuid_pk]
    email: Mapped[str] = mapped_column(VARCHAR(100))
    password: Mapped[str] = mapped_column(VARCHAR(100))
    reg_at: Mapped[time_now]
