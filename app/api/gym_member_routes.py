from fastapi import APIRouter, Depends
from app.dependencies.dependencies import get_gym_member_service
from app.schemas.gym_member_schema import GymMemberCreate, GymMemberResponse, GymMemberUpdate
from app.services.gym_member_service import GymMemberService

router = APIRouter()

@router.get("", response_model=list[GymMemberResponse])
def list_gym_member_endpoint(service: GymMemberService = Depends(get_gym_member_service), skip: int = 0, limit: int = 100):
    return service.get_all_gym_member(skip, limit)

@router.post("", response_model=GymMemberResponse, status_code=201)
def create_gym_member_endpoint(gym_member: GymMemberCreate, service: GymMemberService = Depends(get_gym_member_service)):
    return service.create_gym_member(gym_member)
    
@router.put("/{gym_member_id}", response_model=GymMemberResponse, status_code=200)
def update_gym_member_endpoint(gym_member_id: int, gym_member: GymMemberUpdate, service: GymMemberService = Depends(get_gym_member_service)):
    return service.update_gym_member(gym_member_id, gym_member)

@router.patch("/{gym_member_id}/deactivate", response_model=GymMemberResponse, status_code=200)
def deactivate_gym_member_endpoint(gym_member_id: int, service: GymMemberService = Depends(get_gym_member_service)):
    return service.deactivate_gym_member(gym_member_id)

@router.patch("/{gym_member_id}/activate", response_model=GymMemberResponse, status_code=200)
def activate_gym_member_endpoint(gym_member_id: int, service: GymMemberService = Depends(get_gym_member_service)):
    return service.activate_gym_member(gym_member_id)
    