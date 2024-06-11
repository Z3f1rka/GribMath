import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType
from sqlalchemy_serializer import SerializerMixin


class Achievement_Description(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'achievements_description'

    achievement_id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    picture = sqlalchemy.Column(sqlalchemy.String, nullable=False) # way to file
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    conditions = sqlalchemy.Column(MutableList.as_mutable(PickleType), default=[])