import requests, html

raw_get = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean")
j_data = raw_get.json()
j_data = j_data["results"]
# Clean the data up. 
for i in range(len(j_data)):
    j_data[i]["question"] = html.unescape(j_data[i]["question"])
# print(j_data)

# Let's play with typing.
age: int
name: str
height: float
is_human: bool
# Won't throw an error. It will just change the type since Python has dynamic typing.
age = "twelve"

# It takes an int and returns a bool.
def police_check(age: int) -> bool:
   if age >= 18:
       return True
   else:
       return False

# Throws a type error since it expects an int and you gave it a string.
# police_check("twelve")

# This one works.
police_check(12)