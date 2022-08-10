from datetime import datetime, timedelta
import collections

DAYS_WEEK: dict[int, str] = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Monday",
    7: "Monday"
}


def get_birthdays_per_week(users: list[dict[str, str | datetime]]):
    today = datetime.now()
    w_day = datetime.isoweekday(today)
    start_day = (today + timedelta(days=(6-w_day))).toordinal()
    end_day = start_day + 7
    interval_birthday = [datetime.fromordinal(
        d) for d in range(start_day, end_day)]
    birthday_list = collections.defaultdict(list)

    for user in users:
        for date in interval_birthday:
            if user["birthday"].month == date.month and user["birthday"].day == date.day:
                day_week = DAYS_WEEK[datetime.isoweekday(date)]
                birthday_list[day_week].append(user["name"])

    print("\nUsers to congratulate next week:")
    for i, n in birthday_list.items():
        print("    {:<10}: {:<}".format(i, ', '.join(n)))


if __name__ == "__main__":

    users: list[dict[str, str]] = [
        {"name": "Maksym", "birthday": "12.08.1989"},
        {"name": "Kiril", "birthday": "13.08.1994"},
        {"name": "Gleb", "birthday": "14.08.1992"},
        {"name": "Irina", "birthday": "15.08.1992"},
        {"name": "Sveta", "birthday": "16.08.1992"},
        {"name": "Pavel", "birthday": "17.08.1990"},
        {"name": "Dasha", "birthday": "17.08.1991"},
        {"name": "Sasha", "birthday": "19.08.1994"},
        {"name": "Zara", "birthday": "20.08.1992"},
        {"name": "Zarina", "birthday": "17.09.1992"}
    ]

    for user in users:
        user['birthday'] = datetime.strptime(
            user['birthday'], "%d.%m.%Y")

    get_birthdays_per_week(users)
