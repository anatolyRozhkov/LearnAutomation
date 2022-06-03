import random
import string
import datetime


def random_phone(phone_length):
    return ''.join(random.SystemRandom().choice(string.digits)
                   for _ in range(phone_length))


def random_fake_email():
    variable_value = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(9))
    return variable_value + "@selenium.test"


def random_string():
    variable_value = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(10))
    return variable_value


def random_country_number():
    variable_value = ''.join(random.SystemRandom().choice(string.digits) for _ in range(2))
    return variable_value


def random_date():
    start_date = datetime.date.today().replace(day=1, month=1).toordinal()
    end_date = datetime.date.today().toordinal()
    random_day = datetime.date.fromordinal(random.randint(start_date, end_date))

    date_with_numbers = datetime.datetime.strptime(f"{random_day}", '%Y-%m-%d').strftime('%d.%m.%Y')
    date_with_words = datetime.datetime.strptime(f"{random_day}", '%Y-%m-%d').strftime('%B %d, %Y')

    return [date_with_words, date_with_numbers]