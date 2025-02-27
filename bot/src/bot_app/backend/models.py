import datetime
from typing import Optional, Annotated

from pydantic import BaseModel, Field


class NotiOwner(BaseModel):
    telegram_id: Annotated[str, Field(max_length=12)]


class Contact(BaseModel):
    title: Annotated[str, Field(max_length=40)]
    phone: Optional[Annotated[str, Field(max_length=20)]]
    telegram_id: Optional[Annotated[str, Field(max_length=12)]]
    telegram_username: Optional[Annotated[str, Field(max_length=20)]]


class NotiType(BaseModel):
    title: Annotated[str, Field(max_length=20)]


class Notification(BaseModel):
    title: Annotated[str, Field(max_length=100)]
    owner: NotiOwner
    noti_type: NotiType
    contact: Contact
    time: Optional[Annotated[datetime.time, Field(description='Noti time')]]
    date: Optional[Annotated[datetime.date, Field(description='Noti date')]]
    weekday: Optional[Annotated[int, Field(description='Noti weekday')]]
    periodic: Annotated[bool, Field(description='Noti periodic')] = False
