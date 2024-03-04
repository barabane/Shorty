from models.BaseModel import BaseModel, time_now
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class Visit(BaseModel):
    __tablename__ = "visit"

    url_id: Mapped[str] = mapped_column(ForeignKey('url.id'))
    user_ip: Mapped[str]
    visit_time: Mapped[time_now]
