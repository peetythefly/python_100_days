# import smtplib

# my_email = "sandboxofpatrick@gmail.com"
# psswd = "crtmeahoyxtznpoj"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=psswd)
#     connection.sendmail(from_addr=my_email, to_addrs="peetythefly@gmail.com", msg="Subject:Hello My Name is Inigo Montoya\n\nWazzuuuuuuuup. It's the body of the email now.")

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# # You can get lots of attributes.
# month = now.month
# # Some methods
# weekday = now.weekday()
# # print(weekday)

# dob = dt.datetime(year=1985, month=12, day=1)
# print(dob)

# Lets do stuff on a Monday. Send a quote.
import smtplib, random
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
my_email = "sandboxofpatrick@gmail.com"
psswd = "crtmeahoyxtznpoj"
# Monday is day 0
monday = 0
if weekday == 2:
    with open(file="quotes.txt") as q_file:
        lines = q_file.readlines()
        line = random.choice(lines)
    print(line)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=psswd)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="peetythefly@gmail.com", 
            msg=f"Subject:Inspiration Quote\n\n{line}"
            )
