from sqlalchemy.orm import Session
from app.models.gym_member_model import GymMember
from app.schemas.gym_member_schema import GymMemberCreate

class GymMemberRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_all_gym_members(self, skip: int = 0, limit: int = 100):
        return self.db.query(GymMember).offset(skip).limit(limit).all()
    
    def get_by_id(self, gym_member_id) -> GymMember | None:
        return self.db.query(GymMember).filter(GymMember.id == gym_member_id).first()
    
    def cpf_already_exists(self, cpf: str) -> bool:
        return self.db.query(GymMember).filter(GymMember.cpf == cpf).first() is not None
    
    def create(self, gym_member: GymMemberCreate):
        db_member = GymMember(**gym_member.model_dump())
        self.db.add(db_member)
        self.db.commit()
        self.db.refresh(db_member)
        return db_member
    
    def update(self, gym_member: GymMember):
        self.db.commit()
        self.db.refresh(gym_member)
        return gym_member
    
    def deactivate(self, gym_member: GymMember):
        gym_member.active = False
        self.db.commit()
        self.db.refresh(gym_member)
        return gym_member
    
    def activate(self, gym_member: GymMember):
        gym_member.active = True
        self.db.commit()
        self.db.refresh(gym_member)
        return gym_member
