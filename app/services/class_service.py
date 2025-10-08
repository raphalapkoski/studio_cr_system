from sqlalchemy.orm import Session
from app.models.class_model import Class
from app.models.gym_member_model import GymMember
from app.repositories.class_repository import ClassRepository
from app.repositories.gym_member_repository import GymMemberRepository
from app.schemas.class_schema import ClassCreate

class ClassService:
    def __init__(self, db: Session):
        self.repo = ClassRepository(db)
        self.repo_gym_member = GymMemberRepository(db)
    
    def get_all_classes(self, skip: int = 0, limit: int = 100):
        return self.repo.get_all_classes(skip=skip, limit=limit) 
    
    def create_class(self, createClass: ClassCreate):     
        return self.repo.create(createClass)
    
    def add_gym_member_to_class(self, gym_member_id: int, class_id: int):
        current_class = self.__get_class_by_id(class_id)
        current_gym_member = self.__get_gym_member_by_id(gym_member_id)
        return self.repo.add_gym_member_to_class(current_gym_member, current_class)
    
    def delete_gym_member_to_class(self, gym_member_id: int, class_id: int):
        current_class = self.__get_class_by_id(class_id)
        current_gym_member = self.__get_gym_member_by_id(gym_member_id)
        return self.repo.delete_gym_member_to_class(current_gym_member, current_class)
        
    def __get_class_by_id(self,class_id: int) -> Class:
        current_class = self.repo.get_by_id(class_id=class_id)
        if not current_class:
            raise ValueError("Aula não encontrada")
        return current_class
    
    def __get_gym_member_by_id(self, gym_member_id: int) -> GymMember:
        current_gym_member = self.repo_gym_member.get_by_id(gym_member_id=gym_member_id)
        if not current_gym_member:
            raise ValueError("Aluno não encontrado")
        return current_gym_member