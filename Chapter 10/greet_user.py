import json

filename = 'Chapter 10/username.json'

with open(filename) as f:
    username = json.load(f)
    print("Welcome back, " + username + "!")