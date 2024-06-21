import random

class User:
    def __init__(self, name):
        self.id = random.randrange(10000)
        self.name = name
        self.manager_id = 0

    def add_manager(self, manager):
        self.manager_id = manager.id

user_1 = User("John")
print("John")
print(user_1.id)
user_1.username = "jcarter"

user_2 = User("Jack")
user_2.username = "jblack"
print("Jack")
print(user_2.id)

user_2.add_manager(user_1)

print(f"The id of the manager of {user_2.name} is {user_2.manager_id}")