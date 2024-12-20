import datetime
import json
def add_birthday(birthdays, name, date):
    birthdays[name] = date
    return birthdays
def save_birthdays(birthdays, filename='birthdays.json'):
    with open(filename, 'w') as f:
        json.dump(birthdays, f)
def load_birthdays(filename='birthdays.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
birthdays = {}
birthdays = add_birthday(birthdays, "Alice", "1990-05-15")
birthdays = add_birthday(birthdays, "Bob", "1985-12-31")
print(birthdays)  
save_birthdays(birthdays)
loaded_birthdays = load_birthdays()
print(loaded_birthdays)  
