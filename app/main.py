from fastapi import FastAPI
from app.routers import auth, tests, users
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(tests.router)
app.include_router(users.router)
