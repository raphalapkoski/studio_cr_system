from fastapi import APIRouter, Depends
from app.dependencies.dependencies import get_gym_member_service
from app.schemas.gym_member_schema import GymMemberCreate, GymMemberResponse
from app.services.gym_member_service import GymMemberService

router = APIRouter()

@router.get("/", response_model=list[GymMemberResponse])
def list_students(service: GymMemberService = Depends(get_gym_member_service), skip: int = 0, limit: int = 100):
    return service.get_all_gym_member(skip, limit)

@router.post("/", response_model=GymMemberResponse, status_code=201)
def create_student_endpoint(gym_member: GymMemberCreate, service: GymMemberService = Depends(get_gym_member_service)):
        return service.create_gym_member(gym_member)