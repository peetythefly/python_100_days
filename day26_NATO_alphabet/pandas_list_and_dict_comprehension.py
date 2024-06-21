# Playing with dict comprehension 1. Give the number of letters of each word in a sentence including punctuation.
sentence = "What is the Airspeed Velocity of an unladen swallow?"
sentence = sentence.split()
result = {word:len(word) for word in sentence}
# print(result)

# Playing with dict comprehension 2. Convert Celsius to Farenheit.
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:((temp*9/5)+32) for (day, temp) in weather_c.items()}

# print(weather_f)


# Now do something similar with pandas.
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 89]
}
# Looping through dictionaries.
# for (key, value) in student_dict:
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame.
# for (key, value) in student_data_frame.items():
#     print()

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)
