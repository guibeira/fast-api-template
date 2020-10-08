import uuid

from sqlalchemy.dialects.postgresql import UUID

from {{cookiecutter.project_slug}}.main import db


class User(db.Model):
    __tablename__ = "users_user"

    id = db.Column(UUID(), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(255), nullable=False, index=True)
    is_active = db.Column(db.Boolean, nullable=False)
    username = db.Column(db.String(64), index=True, nullable=False)
    password = db.Column(db.String(248), nullable=False)
