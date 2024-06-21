# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Keep going if divisible by 4.
if year % 4 == 0:
  # The exception is if it's divisble by 400
  if year % 400 == 0:
    print ("Leap year")
  # Stop if divisble by 100
  elif year % 100 == 0:
    print ("Not leap year")
  else:
    print ("Leap year")
else:
  print ("Not leap year")
