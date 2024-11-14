from db_models.user_model import UserModel
from sqlalchemy.orm import Session
from dto import dtos

def create_user(data: dtos.UserDTO, db):
    user = UserModel(name=data.name)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)

    except Exception as e:
        print(e)

    return user

def get_user(id: int, db):
    return db.query(UserModel).filter(UserModel.id == id).first()

def update(data: dtos.UserDTO, db: Session, id: int):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    print(user)
    print(data)
    user.name = data.name
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def remove(db: Session, id: int):
    user = db.query(UserModel).filter(UserModel.id == id).delete()
    db.commit()
    return user