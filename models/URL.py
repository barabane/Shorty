from models.BaseModel import BaseModel, uuid_pk, time_now
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class URL(BaseModel):
    __tablename__ = "url"

    id: Mapped[uuid_pk]
    full_path: Mapped[str]
    short_path: Mapped[str] = mapped_column(unique=True)
    created_at: Mapped[time_now]
    updated_at: Mapped[time_now]
