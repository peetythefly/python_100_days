import datetime as dt
import pandas as pd
import random, smtplib

S_EMAIL = "sandboxofpatrick@gmail.com"
S_PASS = "crtmeahoyxtznpoj"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

bday_df = pd.read_csv("birthdays.csv")

# Use dictionary comprehension syntax for getting the dataframe to the dict.
bday_dict = {(row.month, row.day): row for (index, row) in bday_df.iterrows()}

l_no = random.randint(1, 3)

if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    path = f"letter_templates/letter_{l_no}.txt"
    with open(path) as l_file:
        text = l_file.read()
        text = text.replace("[NAME]", bday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(S_EMAIL, S_PASS)
        connection.sendmail(from_addr=S_EMAIL, 
                            to_addrs=bday_person["email"], 
                            msg=f"Subject:Happy Birthday!\n\n{text}"
                            )