import datetime as dt
import pandas
import random
import smtplib

MONTHS_OF_YEAR = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}
DAYS_OF_WEEK = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6,
}
RANDOM_LETTER_NUMBERS = [
    1,
    2,
    3,
]
PLACEHOLDER = '[NAME]'
SMTP_SERVER_ADDRESS = 'enter server address'
TEST_EMAIL = 'enter sender email'
TEST_EMAIL_PASSWORD = 'enter sender password'

birthdays_df = pandas.read_csv(filepath_or_buffer='./birthdays.csv')
birthdays_list = birthdays_df.values.tolist()

current_month = dt.datetime.now().month
today = dt.datetime.now().day

name = birthdays_list[0][0]
email = birthdays_list[0][1]
birth_month = birthdays_list[0][3]
birth_day = birthdays_list[0][4]

random_letter_number = random.choice(RANDOM_LETTER_NUMBERS)

if current_month == birth_month:
    if today == birth_day:
        with open(file=f'./letter_templates/letter_{random_letter_number}.txt', mode='r') as birthday_wish_file:
            birthday_wish_template = birthday_wish_file.read()
            custom_message = birthday_wish_template.replace(PLACEHOLDER, name)

        with smtplib.SMTP(host=SMTP_SERVER_ADDRESS) as connection:
            receiver_email = email

            connection.starttls()
            connection.login(user=TEST_EMAIL, password=TEST_EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=TEST_EMAIL,
                to_addrs=receiver_email,
                msg='Subject:Happy Birthday\n\n' +
                    custom_message
            )
