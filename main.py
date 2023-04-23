from datetime import datetime, timedelta, date


def check_week(week_dates):
    this_week = []
    for date in week_dates:
        this_week.append(date.strftime( '%d %m'))
    return this_week
    
    
def get_next_week_dates():
    today = datetime.today().date()
    #today = date(2023, 4, 16)
    week_dates = []
    if today.strftime("%A") == 'Sunday':
        for multiplier in range(-1, 6):
            week_dates.append(today + timedelta(days=multiplier))
    elif today.strftime("%A") == 'Monday':
        for multiplier in range(-2, 5):
            week_dates.append(today + timedelta(days=multiplier))
    else:    
        for multiplier in range(7):        
            week_dates.append(today + timedelta(days=multiplier))
    return week_dates
    

def edit_user_list(user, week_dates):
    for date in week_dates:
        if user['birthday'].day == date.day:
            if date.strftime("%A") not in ['Saturday', 'Sunday']:
                list_users_birthday[date.strftime("%A")].append(user['name'])
            else:
                list_users_birthday['Monday'].append(user['name'])
            


def get_birthdays_per_week(users):
    week_dates = get_next_week_dates()
    list_dates = check_week(week_dates)
    this_week = check_week(week_dates)
    for user in users:
        user_birthday = user['birthday'].strftime('%d %m')     
        if user_birthday in this_week:
            edit_user_list(user, week_dates)
    for key, value in list_users_birthday.items():
        if len(value):
            string = ''
            for index, name in enumerate(value):
                if len(value) == index + 1:
                    string += name
                else:
                    string += name + ', '
            print(f'{key}: {string}')
   

if __name__ == '__main__':
    users = [{'name': 'Alex','birthday': datetime(1993, 2, 21)},
             {'name': 'Steve','birthday': datetime(1992, 4, 21)},
             {'name': 'Ray','birthday': datetime(1993, 4, 22)},
             {'name': 'Anna','birthday': datetime(1993, 4, 23)},
             {'name': 'Bill','birthday': datetime(1993, 4, 25)},
             {'name': 'Met','birthday': datetime(1993, 4, 26)},
             {'name': 'Jay','birthday': datetime(1993, 4, 27)}
    ]
    list_users_birthday = {'Monday': [],
                           'Tuesday': [],
                           'Wednesday': [],
                           'Thursday': [],
                           'Friday': [],
                           'Saturday': [],
                           'Sunday': []
    }
    get_birthdays_per_week(users)