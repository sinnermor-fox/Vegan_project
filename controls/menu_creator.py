from werkzeug.exceptions import abort

from app import db, session
from controls.algorithms.create_vegan import count_menu
from models.food import Food
from models.menu_week import MenuWeek
from models.users import User


def create_menu_manual(person_id: int):

    # Конструкция типа User.query ... - ?????
    existing_person = session.query(User).filter(User.id == person_id).first()

    if existing_person is not None:

        # Хотелось бы чтобы метод которым расчитывается меню был задан глобально на уровне приложения
        # или передавался бы через параметр, планируется несколько значений
        food_menu_precounted = count_menu(name='based_csv')

        # Готовим полученные данные для записи в бд

        food_items = []
        for item in food_menu_precounted:
            menu_item = MenuWeek(user_id=person_id, food_id=item.id, netto=1)
            food_items.append(menu_item)
        # Add the person to the database
        db.session.add_all(food_items)
        db.session.commit()

    else:
        abort(404, f'Person with id {person_id} does not exists')


def get_menu_dressed(username):
    user_data = session.query(User).filter(User.telegram_account==username).first()
    menu = session.query(MenuWeek, Food.description).filter(MenuWeek.user_id==user_data.id).all()
    return menu
# create_menu_manual(1)
