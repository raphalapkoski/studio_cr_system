from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.gym_member_class_model import gym_member_class_table

class Class(Base):
    __tablename__ = "class"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    schedule = Column(String, nullable=False)
    total_members = Column(Integer, nullable=False)
    
    gym_members = relationship("GymMember", secondary=gym_member_class_table, back_populates="classes")