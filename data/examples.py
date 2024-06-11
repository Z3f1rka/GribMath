import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Example(SqlAlchemyBase):
    __tablename__ = 'examples'

    problem_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   primary_key=True, autoincrement=True)
    problem = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    answer = sqlalchemy.Column(sqlalchemy.String, unique=False, nullable=False)
    # category_id + category
    category_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("category.category_id"))
    steps = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    category = orm.relationship("Category")
    history = orm.relationship("History", back_populates="example")

