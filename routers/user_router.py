from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import user_service as UserService
from dto.dtos import UserDTO

TAG = "user_tag"

router = APIRouter()

@router.post('/', tags=[TAG])
async def create(data: UserDTO = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)

@router.get('/{id}', tags=[TAG])
async def get(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)

@router.put('/{id}', tags=[TAG])
async def update(id: int = None, data: UserDTO = None, db: Session = Depends(get_db)):
    return UserService.update(data, db, id)

@router.delete('/{id}', tags=[TAG])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.remove(db, id)