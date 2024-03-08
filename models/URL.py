from models.BaseModel import BaseModel, uuid_pk, time_now
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, VARCHAR, ForeignKey


class URL(BaseModel):
    __tablename__ = "url"

    id: Mapped[uuid_pk]
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    full_path: Mapped[str] = mapped_column(Text)
    short_path: Mapped[str] = mapped_column(VARCHAR(25), unique=True)
    created_at: Mapped[time_now]
    updated_at: Mapped[time_now]
