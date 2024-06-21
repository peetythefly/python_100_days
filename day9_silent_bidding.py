import os
gavel = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print (f"{gavel}Welcome to the silent bidding platform.")
# Initialize a dictionary to keep the bidders in
bidders = {}
# Function to add a bidder
def add_bidder(bid_name, bid_number):
    bidders[bid_name] = bid_number

# Loop through each user and add them as a dictionary element of the list.
keep_bidding = True
while keep_bidding:
    # Get name
    name = input("What is your name?\n")
    # Get bid
    bid = int(input("How much are you bidding?\n$"))
    add_bidder(name, bid)
    # Ask if there are more bids and keep going until there are no more.
    more_bidders = input("Are there any more bidders? 'y' or 'n'\n").lower()
    os.system('clear')
    if more_bidders != 'y':
        keep_bidding = False

# Loop through the existing bids and remember what the high is.
high = ""
# Add the high bidder into the dict as 0
bidders[high] = 0
for key in bidders:
    # Check if the current bidder is higher than the high.
    if bidders[key] > bidders[high]:
        bidders[high] = bidders[key]
        high = key
# Print the high bid.
print (f"{high} has the high bid at ${bidders[high]}")