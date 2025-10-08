from fastapi import APIRouter, Depends
from app.dependencies.dependencies import get_class_service
from app.schemas.class_schema import ClassResponse, ClassCreate, ClassUpdate
from app.services.class_service import ClassService

router = APIRouter()

@router.get("", response_model=list[ClassResponse])
def list_class_endpoint(service: ClassService = Depends(get_class_service), skip: int = 0, limit: int = 100):
    return service.get_all_classes(skip, limit)

@router.post("", response_model=ClassResponse, status_code=201)
def create_class_endpoint(class_create: ClassCreate, service: ClassService = Depends(get_class_service)):
    return service.create_class(class_create)

@router.put("/{class_id}", response_model=ClassResponse, status_code=201)
def update_class_endpoint(class_id: int, class_update: ClassUpdate, service: ClassService = Depends(get_class_service)):
    return service.update_class(class_id, class_update)

@router.post("/{class_id}/add-gym-member/{gym_member_id}", response_model=ClassResponse)
def add_gym_member_to_class_endpoint(class_id: int, gym_member_id: int, service: ClassService = Depends(get_class_service)):
    return service.add_gym_member_to_class(gym_member_id, class_id)

@router.post("/{class_id}/delete-gym-member/{gym_member_id}", response_model=ClassResponse)
def delete_gym_member_to_class_endpoint(class_id: int, gym_member_id: int, service: ClassService = Depends(get_class_service)):
    return service.delete_gym_member_to_class(gym_member_id, class_id)