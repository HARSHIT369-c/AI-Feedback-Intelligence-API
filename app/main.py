from fastapi import FastAPI , Depends
from app.database import engine , Base  , SessionLocal
from app.routes import user

app = FastAPI(
    description="AI Feedback Intelligence API",
    version="1.0.0",
    title="AI_API"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message":"welcome to AI Feedback Intelligence API"}

@app.get("/health")
def health_cheack():
    return {"status":"OK"}

app.include_router(user.router , prefix="/users" , tags=["Users"])