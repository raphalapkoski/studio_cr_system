from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base

gym_member_class_table = Table(
    "gym_member_class",
    Base.metadata,
    Column("gym_member_id", Integer, ForeignKey("gym_member.id"), primary_key=True),
    Column("class_id", Integer, ForeignKey("class.id"), primary_key=True)
)
