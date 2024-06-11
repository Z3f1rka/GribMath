import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class History(SqlAlchemyBase):
    __tablename__ = 'history'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    is_solved = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    # history + user_id
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')
    # history + problem_id
    problem_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("examples.problem_id"))
    example = orm.relationship("Example")

    