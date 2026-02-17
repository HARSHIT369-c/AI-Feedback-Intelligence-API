from fastapi import FastAPI

app = FastAPI(
    description="AI Feedback Intelligence API",
    version="1.0.0",
    title="AI_API"
)

@app.get("/")
def home():
    return {"message":"welcome to AI Feedback Intelligence API"}

@app.get("/health")
def health_cheack():
    return {"status":"OK"}