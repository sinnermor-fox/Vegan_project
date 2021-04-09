import datetime

from werkzeug.exceptions import abort

from app import db
from src.controls.algorithms.create_vegan import count_menu
from src.models.food import Food
from src.models.menu_week import MenuWeek
from src.models.users import User


def create_day_menu_manual(user_account: str, day=1):
    person = User.query.filter(User.telegram_account == user_account).first()
    if check_ready_menu(user_account, day):
        if person is not None:
            food_menu_pre_counted = count_menu(name='based_csv')
            food_items = []
            for item in food_menu_pre_counted:
                menu_item = MenuWeek(user_id=person.id,
                                     food_id=item.id,
                                     netto=1,
                                     day_id=day)
                food_items.append(menu_item)
            db.session.add_all(food_items)
            db.session.commit()
            return {'status': f'Success',
                'status_code': 201}
        else:
            abort(406, f'Person with id {person.id} does not exists')
            return {'status': f'Person with id {person.id} does not exists',
                    'status_code': 499}
    else:
        return {'status': f'Menu for day {day} alredy exsists',
                'status_code': 499}


def check_ready_menu(user_account: str, day: int):
    today = datetime.date.today()
    user = User.query.filter(
        User.telegram_account == user_account
    ).first()
    today_menu = MenuWeek.query.filter(
        MenuWeek.user_id == user.id,
        MenuWeek.creation_date == today,
        MenuWeek.day_id == day
    ).all()
    if today_menu:
        return False
    else: return True


def get_menu_dressed(user_account: str, day="today"):
    """Method for get week menu for user"""
    user_data = User.query.filter(
        User.telegram_account == user_account
    ).first()
    query = db.session.query(
            MenuWeek,
            User,
            Food.description
        ).filter(
            MenuWeek.user_id == user_data.id,
        ).filter(
            MenuWeek.food_id == Food.id
        )
    if day == 'today':
        menu = query.filter(
            MenuWeek.creation_date == datetime.date.today()
        ).all()
    else:
        week_day = datetime.date.today() - datetime.timedelta(6)
        menu = query.filter(
            MenuWeek.creation_date >= week_day
        ).all()
    return menu


def create_menu_week(user_account: str):
    """Method to create menu for 1 user for a week"""
    result = []
    week_day = datetime.date.today().weekday()
    for day in range(week_day, 7):
        menu_statuses = create_day_menu_manual(user_account, day)
        if menu_statuses["status_code"] != 201:
            result.append(menu_statuses)
    return result


