# Samples of Error Types

# File not found error
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["not_a_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)


# How do we catch these exceptions?
# We can use try, except, else, and finally

# File not found error
# Do something where you think you might get an exception.
# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# # Do this if there is an error/exception. 
# # except:  This catches all exceptions if you don't specify.
# except FileNotFoundError:
#     # You could put the alternative if the above fails.
#     # If that file does not exist that you're trying to open, then create it.
#     file = open("a_file.txt", "w")
#     file.write("Who do you think you are Mr. Big Stuff?")
# except KeyError as error_msg:
#     print("No key")
#     print(f"The key missing is {error_msg}")
# # Do this if there are no exceptions.
# else:
#     content = file.read()
#     print(content)
# # Do this no matter what happens.
# finally:
#     file.close()
#     print("File was closed.")
# # Generating your own exceptions.
#     raise TypeError("I am chaos incarnate!")

# # Generating your own exceptions.
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human heigh should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)