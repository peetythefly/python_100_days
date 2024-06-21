import random
# score = 0
# height = 1.8
# isWinning = True
# f-String
# print (f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# integer = random.randint(1, 10)
# print (integer)

# file = open ('scrapeme.txt', 'r')

# for data in file:
#     if data.startswith("prometheus"):
#         print (data)
# print (file.readline(),end="\n")

#travel_log = {
#    "France": {"cities_visited": ["Paris", "Lillie", "Dijon"], "total_visits": 12}, 
#    "Germany": {"cities_visited": ["Berlin", "Haamburg", "Stuttgart"],
#                "beer_drank": {
#                    "Stout": "Excellent",
#                    "Dopplebock": "Delicious",
#                    "Lager": "Good"
#                }},
#}
#
#print (travel_log ["Germany"]["beer_drank"]["Stout"])

# travel_log = [
#     {
#         "country": "France", 
#         "cities_visited": ["Paris", "Lillie", "Dijon"], 
#         "total_visits": 12
#     }, 
#     {
#         "country": "Germany", 
#         "cities_visited": ["Berlin", "Haamburg", "Stuttgart"], 
#         "total_visits": 7
#     },
# ]
# 
# Oh look, you can have any value type
# blarg = ["test", 13, False]
# print (blarg[2])

# Can you put different element types in a list?
# blarg = ["Joe", 123]
# print (blarg)
# blarg[1] = "John"
# print (blarg)

# Docstring
# def format_name(f_name, l_name):
#     """This is a function that takes in two names (first, then last).
#      It will format those names so that the first letter is capitalized and the rest of the letters are lower-cased."""
#     first = f_name.title()
#     last = l_name.title()
#     return (first + " " + last)
# print (format_name("john","CARTER"))

# nums = [3, 3]
# target = 6
# for i in nums:
#     for j in nums:
#         index_i = nums.index(i)
#         index_j = nums.index(j)
#         print (f"i is {i} and j is {j}")
#         print (f"i index is {index_i} and j index is {index_j}")
#         if index_i != index_j:
#             if (i + j) == target:
#                 print ([index_i, index_j])

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# contacts = {
#     "James" : {
#         "phone_number" : 8675309,
#         "email" : "dontstartmeup@hotmail.com",
#     },
#     "Ogre" : {
#         "phone_number" : 1234567,
#         "email" : "susie_is_watching@hotmail.com",
#     }
# }
# print (contacts["James"]["phon_number"])
# 
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         print (l1)
# 
# 
# def my_add(n1, n2):
#     total = n1 + n2
#     return total
# 
# 
# my_add(4, 5)
# for _ in range(100):
#     print("Hello") 

obj_list = ["A", "B", "C", "D", "E"]


# dct = {}
# for obj in obj_list:
#     dct[obj] = 0


# for _ in range(100):
#     # print(random.choice(obj_list))
#     recv_obj = random.choice(obj_list)
#     dct[recv_obj] += 1
# print(dct)
# That's kind of tedious. Let's do it with a counter now.
# from collections import Counter
# counter = Counter()
# for _ in range(100):
#     taken_obj = random.choice(obj_list)
#     counter[taken_obj] += 1
# print(counter)
# print(counter.most_common(3))

# occurences = random.choices(obj_list, k=100)
# print(occurences)