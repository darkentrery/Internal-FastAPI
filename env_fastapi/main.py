import uvicorn
from fastapi import FastAPI

from env_fastapi.controllers import main as UserRouter
from env_fastapi.controllers.main import fastapi_users
from env_fastapi.dto.user import UserCreateDTO, UserGetDto
from env_fastapi.services.auth import auth_backend


app = FastAPI()
app.include_router(UserRouter.router, prefix="/user")

app.include_router(
    fastapi_users.get_register_router(UserGetDto, UserCreateDTO),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
