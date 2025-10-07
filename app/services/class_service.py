from sqlalchemy.orm import Session
from app.repositories.class_repository import ClassRepository
from app.schemas.class_schema import ClassCreate

class ClassService:
    def __init__(self, db: Session):
        self.repo = ClassRepository(db)
    
    def get_all_classes(self, skip: int = 0, limit: int = 100):
        return self.repo.get_all_classes(skip=skip, limit=limit) 
    
    def create_class(self, createClass: ClassCreate):     
        return self.repo.create(createClass)