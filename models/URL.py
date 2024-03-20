from sqlalchemy import Text, VARCHAR, ForeignKey, INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from models.BaseModel import BaseModel, time_now


class URL(BaseModel):
    __tablename__ = "url"

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    full_path: Mapped[str] = mapped_column(Text)
    short_path: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    created_at: Mapped[time_now]
    updated_at: Mapped[time_now]
