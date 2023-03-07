from datetime import date, datetime, timedelta
from users import users


result = {
    "monday": [],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": []
}


def get_birthdays_per_week(users):

    for user in users:
        birthday_this_year = define_birthday_this_year(user)

        if check_user_has_birthday_nextweek(birthday_this_year):
            
            weekday= define_weekday(birthday_this_year)
            put_user_in_result_table(user["name"], weekday)

    print_birthday_people()                


def define_birthday_this_year(user):
    return user["birthday"].replace(year=datetime.now().year)


def define_weekday(date):
    weekday = date.strftime("%A").lower()
    if weekday not in result.keys():
        return "monday"
    return weekday


def check_user_has_birthday_nextweek(birthday):

    day_from, day_to = define_birthday_week()
    if day_from < birthday <= day_to:
        return True
    return False


def define_birthday_week():
    
    current_day = datetime.now().date()
    current_weekday = current_day.weekday()
    delta = 5 - current_weekday
    day_from = current_day + timedelta(days=delta)
    day_to = day_from + timedelta(days=6)

    return day_from, day_to


def print_birthday_people():
    with open("birthdays.txt", "w") as fh:
        for day, users in result.items():
            if users:
                fh.write(f"{day}: {', '.join(users)}\n")


def put_user_in_result_table(username, weekday):
    result[weekday].append(username)


if __name__ == '__main__':
    get_birthdays_per_week(users)
