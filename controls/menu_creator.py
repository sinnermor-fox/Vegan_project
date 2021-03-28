from werkzeug.exceptions import abort

from app import db
from controls.algorithms.create_vegan import count_menu
from models.food import Food
from models.menu_week import MenuWeek
from models.users import User


def create_menu_manual(person_id: int):
    existing_person = User.query().filter(User.id == person_id).first()
    if existing_person is not None:
        # Хотелось бы чтобы метод которым расчитывается меню был задан глобально на уровне приложения
        # или передавался бы через параметр, планируется несколько значений
        food_menu_pre_counted = count_menu(name='based_csv')
        food_items = []
        for item in food_menu_pre_counted:
            menu_item = MenuWeek(user_id=person_id, food_id=item.id, netto=1)
            food_items.append(menu_item)
        db.session.add_all(food_items)
        db.session.commit()

    else:
        abort(406, f'Person with id {person_id} does not exists')


def get_menu_dressed(username: str):
    user_data = User.query.filter(
        User.telegram_account == username
    ).first()
    menu = db.session.query(
        MenuWeek,
        User,
        Food.description
    ).filter(
        MenuWeek.user_id == user_data.id
    ).filter(
        MenuWeek.food_id == Food.id
    ).all()
    return menu
