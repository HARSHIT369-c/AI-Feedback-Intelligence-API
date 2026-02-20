from fastapi import FastAPI , Depends
from app.database import engine , Base  , SessionLocal
from app.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

app = FastAPI(
    description="AI Feedback Intelligence API",
    version="1.0.0",
    title="AI_API"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message":"welcome to AI Feedback Intelligence API"}

@app.get("/health")
def health_cheack():
    return {"status":"OK"}

@app.post("/create_user")
def create_user(email :str , password :str , db:Session = Depends(get_db)):
    new_users = User(email=email , password_hash = password)
    try:
       db.add(new_users)
       db.commit()
       db.refresh(new_users)
       return {"message":"user created" , "id":new_users.id}
    except IntegrityError:
       db.rollback()
       raise HTTPException(status_code=400 , detail = "Email already exists")