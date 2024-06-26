import requests, auth
import datetime as dt

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

graph_headers = {
    "X-USER-TOKEN": auth.pixela_api_key,
}

value_endpoint = f"{pixela_endpoint}/{auth.pixela_user}/graphs/{GRAPH_ID}"
value_headers = {
    "X-USER-TOKEN": auth.pixela_api_key,
}
# We want the format yyyyMMdd.
now = dt.datetime.now().strftime('%Y%m%d')
value_params = {
    "date": now,
    "quantity": "1",
}
# Create a user. Only need to run it one time.
# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

# Create a graph. Only need to run it one time.
# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=graph_headers)
# print(response.text)

# Post a value to the graph.
response = requests.post(url=value_endpoint, json=value_params, headers=value_headers)
print(response.text)