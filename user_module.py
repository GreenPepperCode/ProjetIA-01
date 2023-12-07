from getpass import getpass # Module to hide user password's accounts
import json

def create_account():
    # user boilerplate to generate new users
    with open("users-data.json", "r") as json_data:
        json_db = json.load(json_data)
        new_user = json_db["boiler-plate"].copy()
        list_users = json_db["users"]
    
    # Ask the user for nickname and password
    new_user["nickname"] = input("Nickname : ")
    new_user["password"] = getpass("Password : ")

    list_users.append(new_user)

    with open("users-data.json", "w") as json_data:
        json_db["users"] = list_users
        json.dump(json_db, json_data, indent=4)
    return new_user

def connect():
    nickname = input("Nickname : ")
    password = getpass("Password : ")

    with open("users-data.json", "r") as json_data:
        json_db = json.load(json_data)
        
        for user in json_db["users"]:
            if user["nickname"] == nickname and user["password"] == password:
                return user
        print("Veuillez réessayer de vous connecter ou quitter")    
        return (connect())