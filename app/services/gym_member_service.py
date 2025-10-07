from sqlalchemy.orm import Session
from app.models.gym_member_model import GymMember
from app.repositories.gym_member_repository import GymMemberRepository
from app.schemas.gym_member_schema import GymMemberCreate

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