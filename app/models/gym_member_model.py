from datetime import date, datetime
from sqlalchemy import Boolean, Date, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.gym_member_class_model import gym_member_class_table

class GymMember(Base):
    __tablename__ = "gym_member"
    
    id: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    birth_date: Mapped[date] = mapped_column(Date,nullable=False)
    cpf: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String,nullable=False)
    active: Mapped[bool] = mapped_column(Boolean,default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now(),nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),onupdate=func.now(), nullable=True)
    
    classes = relationship("Class", secondary=gym_member_class_table, back_populates="gym_members")
