import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Bem vindo de volta, " + username + "!")