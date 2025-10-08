from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.gym_member_class_model import gym_member_class_table

class Class(Base):
    __tablename__ = "class"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    schedule: Mapped[str] = mapped_column(String, nullable=False)
    total_members: Mapped[int] = mapped_column(Integer, default=0)
    
    gym_members = relationship("GymMember", secondary=gym_member_class_table, back_populates="classes")