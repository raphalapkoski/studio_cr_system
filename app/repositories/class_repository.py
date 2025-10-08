from sqlalchemy.orm import Session
from app.models.class_model import Class
from app.models.gym_member_model import GymMember
from app.schemas.class_schema import ClassCreate

class ClassRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_classes(self, skip: int = 0, limit: int = 100):
        return self.db.query(Class).offset(skip).limit(limit).all()
    
    def get_by_id(self, class_id: int) -> Class | None:
        return self.db.query(Class).filter(Class.id == class_id).first()
    
    def create(self, classCreate: ClassCreate):
        db_member = Class(**classCreate.model_dump())
        self.db.add(db_member)
        self.db.commit()
        self.db.refresh(db_member)
        return db_member
    
    def add_gym_member_to_class(self, gym_member: GymMember, current_class: Class):
        current_class.gym_members.append(gym_member)
        current_class.total_members -= 1
        self.db.commit()
        self.db.refresh(current_class)
        return current_class