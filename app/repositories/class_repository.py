from sqlalchemy.orm import Session
from app.models.class_model import Class
from app.schemas.class_schema import ClassCreate

class ClassRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all_classes(self, skip: int = 0, limit: int = 100):
        return self.db.query(Class).offset(skip).limit(limit).all()
    
    def create(self, classCreate: ClassCreate):
        db_member = Class(**classCreate.model_dump())
        self.db.add(db_member)
        self.db.commit()
        self.db.refresh(db_member)
        return db_member