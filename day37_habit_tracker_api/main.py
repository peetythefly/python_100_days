import requests, auth
import datetime as dt

# Pixela's API: https://docs.pixe.la/

# The API calls for the format yyyyMMdd.
NOW = dt.datetime.now().strftime('%Y%m%d')
GRAPH_ID = "gymworkouts"

pixela_endpoint = "https://pixe.la/v1/users"
params = {
    "token": auth.pixela_api_key,
    "username": auth.pixela_user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

pixela_graph_endpoint = f"https://pixe.la/v1/users/{auth.pixela_user}/graphs"
graph_params = {
    "id": GRAPH_ID,
    "name": "Gym Workouts",
    "unit": "day",
    "type": "int",
    "color": "shibafu", 
}

headers = {
    "X-USER-TOKEN": auth.pixela_api_key,
}

value_endpoint = f"{pixela_endpoint}/{auth.pixela_user}/graphs/{GRAPH_ID}"
update_endpoint = f"{pixela_endpoint}/{auth.pixela_user}/graphs/{GRAPH_ID}/{NOW}"
update_params = {
    "quantity": "4" # Work out 4 times so we can be totally swo.
}

update_graph_params = {
    "unit": "Hours worked out"
}

# We want it to increase the hours worked out for today by 1 hour.
# First we'll get the quantity that is currently there for today.
# We only want to get the data if there's already a pixel in place for today.
# If there's no existing pixel we set it to 0.
if requests.get(url=update_endpoint, headers=headers):
    hours_today = requests.get(url=update_endpoint, headers=headers).json()
else:
    hours_today = {'quantity': '0'}
# Now every time we run this, it will increase the hours worked out today by 1.
hours_to_update = int(hours_today["quantity"]) + 1
value_params = {
    "date": NOW,
    "quantity": str(hours_to_update),
}

# Post a value to the graph.
response = requests.post(url=value_endpoint, json=value_params, headers=headers)
print(response.text)

# Create a user. Only need to run it one time.
# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

# Create a graph. Only need to run it one time.
# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=graph_headers)
# print(response.text)

