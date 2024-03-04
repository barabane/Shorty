import uuid
import datetime
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import String, DateTime, func
from typing import Annotated


def generated_uuid():
    return str(uuid.uuid4())


uuid_pk = Annotated[str, mapped_column(String(36), primary_key=True, default=generated_uuid)]
time_now = Annotated[datetime.datetime, mapped_column(DateTime(timezone=True), default=datetime.datetime.now(),
                                                      server_default=func.now())]

class BaseModel(DeclarativeBase):
    pass
