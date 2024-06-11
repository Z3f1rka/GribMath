import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class MainCategory(SqlAlchemyBase):
    __tablename__ = 'main_category'

    main_category_id = sqlalchemy.Column(sqlalchemy.Integer,
                                         primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    # category + main_category
    category = orm.relationship("Category", back_populates="main_cat")