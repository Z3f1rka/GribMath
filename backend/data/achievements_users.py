import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Achievement_User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'achievements_users'

    connection_id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    achievement_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("achievements_description.achievement_id"))