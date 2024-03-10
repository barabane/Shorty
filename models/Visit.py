from sqlalchemy import ForeignKey, VARCHAR, INTEGER
from sqlalchemy.orm import Mapped, mapped_column

from models.BaseModel import BaseModel, time_now


class Visit(BaseModel):
    __tablename__ = "visit"

    id: Mapped[int] = mapped_column(INTEGER, autoincrement=True, primary_key=True)
    url_id: Mapped[str] = mapped_column(ForeignKey('url.id'))
    visit_ip: Mapped[str] = mapped_column(VARCHAR(20))
    visit_time: Mapped[time_now]
