from fastapi import FastAPI
from routers import analytics
from fastapi.middleware.cors import CORSMiddleware
#from .database import Base, engine

#Base.metadata.create_all(bind=engine)

app = FastAPI()

#update CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"health_check": "complete"}

app.include_router(analytics.router)

