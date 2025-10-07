from typing import List, Optional
from pydantic import BaseModel
from app.schemas.gym_member_schema import GymMemberResponse

class ClassBase(BaseModel):
    name: str
    schedule: str
    total_members: int

class ClassCreate(ClassBase):
    pass

class ClassResponse(ClassBase):
    id: int
    students: Optional[List[GymMemberResponse]] = []

    model_config = {
        "from_attributes": True,
        "arbitrary_types_allowed": True,
    }