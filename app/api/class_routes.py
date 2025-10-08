from fastapi import APIRouter, Depends
from app.dependencies.dependencies import get_class_service
from app.schemas.class_schema import ClassResponse, ClassCreate
from app.services.class_service import ClassService

router = APIRouter()

@router.get("", response_model=list[ClassResponse])
def list_class_endpoint(service: ClassService = Depends(get_class_service), skip: int = 0, limit: int = 100):
    return service.get_all_classes(skip, limit)

@router.post("", response_model=ClassResponse, status_code=201)
def create_class_endpoint(classCreate: ClassCreate, service: ClassService = Depends(get_class_service)):
    return service.create_class(classCreate)

@router.post("/{class_id}/add-gym-member/{gym_member_id}", response_model=ClassResponse)
def add_gym_member_to_class_endpoint(class_id: int, gym_member_id: int, service: ClassService = Depends(get_class_service)):
    return service.add_gym_member_to_class(gym_member_id, class_id)