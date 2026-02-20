from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.user import userCreate , userResponse
from app.crud.user import create_user , get_user_by_email
from app.core.security import hash_password , verify_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/" , response_model=userResponse)
def register_user(user:userCreate , db:Session = Depends(get_db)):
    existing_user = get_user_by_email(db , user.email)
    if existing_user:
        raise HTTPException(status_code=400 , detail = "Email already exists")
    
    hashed_password = hash_password(user.password)
    new_user = create_user(db , user.email ,hashed_password)
    return new_user

@router.post("/login")
def login_user(user:userCreate , db:Session = Depends(get_db)):
    db_user = get_user_by_email(db , user.email)
    if not db_user:
        raise HTTPException(status_code=400 , detail="Invalid credentails")
    
    if not verify_password(user.password , db_user.password_hash):
        raise HTTPException(status_code=400 , detail="Invalid credentails")
    
    return {"message":"login sucessful"}


