from models.BaseModel import BaseModel, time_now
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, VARCHAR, INTEGER


class Visit(BaseModel):
    __tablename__ = "visit"

    id: Mapped[int] = mapped_column(INTEGER, autoincrement=True, primary_key=True)
    url_id: Mapped[str] = mapped_column(ForeignKey('url.id'))
    visit_ip: Mapped[str] = mapped_column(VARCHAR(20))
    visit_time: Mapped[time_now]
