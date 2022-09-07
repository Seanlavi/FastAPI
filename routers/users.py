import sys

sys.path.append("..")

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from pydantic import BaseModel
import models
from .auth import get_user_exception, verify_password, get_password_hashed, get_current_user

router = APIRouter(
    prefix="/users",
    tags=['users'],
    responses={401: {"user": "user not authorized"}}
)

models.Base.metadata.create_all(bind=engine)


class verifyUser(BaseModel):
    username: str
    password: str
    new_password: str


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/")
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@router.get("/get_user_query")
async def get_user_by_query(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Todos).filter(models.Todos.id == user_id).first()
    if user is not None:
        return user
    raise HTTPException()


@router.get("/{user_id}")
async def get_user_by_path(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Todos).filter(models.Todos.id == user_id).first()
    if user is not None:
        return user
    raise HTTPException()


@router.put("/update_password")
async def update_pass(verified: verifyUser, user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    if user is None:
        raise get_user_exception()
    if user_model.username == verified.username and verify_password(verified.password, user_model.hashed_password):
        user_model.hashed_password = get_password_hashed(verified.new_password)
        db.add(user_model)
        db.commit()
        return "password updated successfully"
    return "not authorised, please try again "


@router.delete("/delete_user")
async def delete_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    user_delete = db.query(models.Users).filter(models.Users.id == user.get("id")).first()
    if user_delete is None:
        return "invalid user or request"
    db.query(models.Users).filter(models.Users.id == user.get("id")).delete()
    db.commit()
    return "user deleted successfully"
