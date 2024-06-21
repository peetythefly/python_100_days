#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
# Get all the input values
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
# Strip out the $ from bill and make it an integer. Do the same for tip % if they did that.
bill = float(bill.replace('$', ''))
tip = float(tip.replace('%', ''))
# Tip is actually percentage
tip = int(tip) / 100
# Calculate the tip amount based on the bill, tip percentage, and the number of people
pay = (bill + (bill * tip)) / int(people)
# Round to 2 digits for $ style
pay = round(pay, 2)
# We really want to always display 2 decimal places no matter what
pay = '{0:.2f}'.format(pay)
# Print the result
print(f"Each person should pay: ${pay}")
