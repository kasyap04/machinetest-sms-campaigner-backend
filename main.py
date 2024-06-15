from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

from app.api import router
from app.config import Config


app = FastAPI(
    title="SMS Campaigner - FastAPI",
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=[Config.FRONTEND_URL],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
)

app.include_router(router)