from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

from controller.auth import AuthController
from app.api import router
from app.config import Config


app = FastAPI(
    title="SMS Campaigner - FastAPI",
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]
)

@app.middleware("http")
async def middle(request: Request, call_next):
    url = request.url.path

    if url not in ["/login", "/logout"]:
        auth    = AuthController()
        request.state.verifyToken = auth.common_validation(request)
        

    response = await call_next(request)
    return response
        


app.include_router(router)


@app.get("/")
def root():
    return "Welcome to SMS Campaigner"