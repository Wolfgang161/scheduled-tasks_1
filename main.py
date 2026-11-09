# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations. Test


import datetime as dt
import pandas
import requests
import os
from dotenv import load_dotenv

# import os and use it to get the Github repository secrets
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_CHATID = os.environ.get("BOT_CHATID")

today= dt.datetime.now()
day = today.day
month = today.month

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dic = pandas.DataFrame.to_dict(birthdays,orient="records")

def send_telegram(telegram_message):
    send_text = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage?chat_id=" + BOT_CHATID + "&parse_mode=Markdown&text=" + telegram_message
    response_tele = requests.get(send_text)
    response_tele.raise_for_status()

for entry in birthdays_dic:
    if month == entry["month"] and day == entry["day"]:
        send_telegram(f"Birthday Alert! It's {entry["name"]}'s birthday.") 
