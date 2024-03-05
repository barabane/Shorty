from models.BaseModel import BaseModel, time_now
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, VARCHAR


class Visit(BaseModel):
    __tablename__ = "visit"

    url_id: Mapped[str] = mapped_column(ForeignKey('url.id'), primary_key=True)
    user_ip: Mapped[str] = mapped_column(VARCHAR(20))
    visit_time: Mapped[time_now]
