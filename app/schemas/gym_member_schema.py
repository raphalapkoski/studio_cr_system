from typing import Optional
from pydantic import BaseModel, field_validator
from datetime import date, datetime

from app.validators.gym_member_validator import GymMemberValidators

class GymMemberBase(BaseModel):
    name: str
    birth_date: date
    cpf: str
    phone: str
    
class GymMemberCreate(GymMemberBase):    
    @field_validator('name')
    @classmethod
    def check_name(cls, v: str) -> str:
        return GymMemberValidators.validate_name_format(v)

    @field_validator('cpf')
    @classmethod
    def check_cpf(cls, v: str) -> str:
        return GymMemberValidators.validate_cpf_format(v)

    @field_validator('phone')
    @classmethod
    def check_phone(cls, v: str) -> str:
        return GymMemberValidators.validate_phone_format(v)
    pass

class GymMemberResponse(GymMemberBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {
        "from_attributes": True,     
        "arbitrary_types_allowed": True,
    }