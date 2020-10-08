import typing

from fastapi import APIRouter, Depends

from .models import User as UserModel
from {{cookiecutter.project_slug}}.apps.auth.authentication import validate_token
from {{cookiecutter.project_slug}}.apps.users.schemas import User
from {{cookiecutter.project_slug}}.pagination import Pagination

router = APIRouter()


@router.get(
    "/users/",
    description="Endpoint to search users",
    response_model=typing.List[User],
    dependencies=[Depends(validate_token)],
)
async def users_search(p: Pagination = Depends()):
    if p.q is None:
        query = UserModel.query.limit(p.limit).offset(p.offset)
    else:
        query = UserModel.query.where(UserModel.username == p.q).limit(p.limit).offset(p.offset)
    users = await query.gino.all()
    return users


def include_router(app):
    app.include_router(router)
