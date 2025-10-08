from sqlalchemy.orm import Session
from app.models.gym_member_model import GymMember
from app.repositories.gym_member_repository import GymMemberRepository
from app.schemas.gym_member_schema import GymMemberCreate, GymMemberUpdate

class GymMemberService:
    def __init__(self, db: Session):
        self.repo = GymMemberRepository(db)
        
    def get_all_gym_member(self, skip: int = 0, limit: int = 100):
        return self.repo.get_all_gym_members(skip=skip, limit=limit)
    
    def create_gym_member(self, gym_member: GymMemberCreate):     
        cpf_already_exists = self.repo.cpf_already_exists(gym_member.cpf)
        if cpf_already_exists:
            raise ValueError("Já existe um registro de aluno para esse CPF")
        return self.repo.create(gym_member)
    
    def update_gym_member(self, gym_member_id: int, gym_member: GymMemberUpdate):
        current_gym_member = self.__get_by_id(gym_member_id)
        updates = gym_member.model_dump(exclude_unset=True)
        current_gym_member.__dict__.update(updates)
        return self.repo.update(current_gym_member)
    
    def deactivate_gym_member(self, gym_member_id: int):
        current_gym_member = self.__get_by_id(gym_member_id)
        return self.repo.deactivate(current_gym_member)
    
    def activate_gym_member(self, gym_member_id: int):
        current_gym_member = self.__get_by_id(gym_member_id)
        return self.repo.activate(current_gym_member)
    
    def __get_by_id(self, gym_member_id: int):
        current_gym_member = self.repo.get_by_id(gym_member_id)
        if not current_gym_member:
            raise ValueError("Aluno não encontrado")
        return current_gym_member