from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.gym_member_service import GymMemberService
from app.services.class_service import ClassService


def get_gym_member_service(db: Session = Depends(get_db)) -> GymMemberService:
    return GymMemberService(db)

def get_class_service(db: Session = Depends(get_db)) -> ClassService:
    return ClassService(db)