from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, func
from app.core.database import Base


class GymMember(Base):
    __tablename__ = "gym_member"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    cpf = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), nullable=True)