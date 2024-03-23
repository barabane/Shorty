import datetime
import uuid
from typing import Annotated

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, mapped_column


def generated_uuid():
    return str(uuid.uuid4())


uuid_pk = Annotated[str, mapped_column(String(36), primary_key=True, default=generated_uuid)]
time_now = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), server_default=func.now())]


class BaseModel(DeclarativeBase):
    pass
