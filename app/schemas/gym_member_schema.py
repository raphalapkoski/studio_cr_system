from typing import Optional
from pydantic import BaseModel, field_validator
from datetime import date, datetime

from app.validators.gym_member_validator import GymMemberValidators

class GymMemberBase(BaseModel):
    name: str
    phone: str
    
    @field_validator('name')
    @classmethod
    def check_name(cls, v: str) -> str:
        return GymMemberValidators.validate_name_format(v)
    
    @field_validator('phone')
    @classmethod
    def check_phone(cls, v: str) -> str:
        return GymMemberValidators.validate_phone_format(v)
        
class GymMemberCreate(GymMemberBase):    
    birth_date: date
    cpf: str
    
    @field_validator('cpf')
    @classmethod
    def check_cpf(cls, v: str) -> str:
        return GymMemberValidators.validate_cpf_format(v)
    
    pass

class GymMemberUpdate(GymMemberBase):    
    pass

class GymMemberResponse(GymMemberBase):
    id: int
    birth_date: date
    cpf: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {
        "from_attributes": True,     
        "arbitrary_types_allowed": True,
    }