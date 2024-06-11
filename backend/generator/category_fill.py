from data import db_session
from data.category import Category
from data.main_category import MainCategory


def db_cat_fill():
    db_session.global_init(r"..\db\users.db")
    db = db_session.create_session()
    main_cat = MainCategory(title="Числовые примеры")
    db.add(main_cat)
    db.commit()
    main_cat = MainCategory(title="Линейные уравнения")
    db.add(main_cat)
    db.commit()
    main_cat = MainCategory(title="Операции с дробями")
    db.add(main_cat)
    db.commit()
    cat = Category(title="Простые", main_category_id=1)
    db.add(cat)
    db.commit()
    cat = Category(title="Средние", main_category_id=1)
    db.add(cat)
    db.commit()
    cat = Category(title="Сложные", main_category_id=1)
    db.add(cat)
    db.commit()
    cat = Category(title="Простые", main_category_id=2)
    db.add(cat)
    db.commit()
    cat = Category(title="Средние", main_category_id=2)
    db.add(cat)
    db.commit()
    cat = Category(title="Сложные", main_category_id=2)
    db.add(cat)
    db.commit()
    cat = Category(title="Простые", main_category_id=3)
    db.add(cat)
    db.commit()
    cat = Category(title="Средние", main_category_id=3)
    db.add(cat)
    db.commit()
    cat = Category(title="Сложные", main_category_id=3)
    db.add(cat)
    db.commit()




if __name__ == "__main__":
    db_cat_fill()