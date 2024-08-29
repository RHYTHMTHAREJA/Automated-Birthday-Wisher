import pandas
from datetime import datetime
import random
import smtplib

my_email = "write your own email"
password = "write your own email app password"

today = datetime.now()
today_tuple = (today.day, today.month)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthday_dict[today_tuple]
    with open(file_path, "r") as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"subject:Happy Birthday\n\n{content}")






