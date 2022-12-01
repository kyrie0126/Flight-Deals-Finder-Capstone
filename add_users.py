# C&P into shareable programming interface like replit. That way, users can add themselves to Google Sheet!!!

import requests
import os


# terminal interface for user addition, could improve with tkinter UI
print("Welcome to Kyle's Flight Club\n")
first_name = input("What's your first name?\n").title()
last_name = input("What's your last name?\n").title()
email = input("What's your email?\n").lower()
check_email = input("Please type your email again:\n").lower()

# Make Sheety API post request to users sheet
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT_USERS"]
SHEETY_BASE64_PASS = os.environ["SHEETY_BASE64_PASS_USERS"]

header = {
    "Authorization": f"Basic {SHEETY_BASE64_PASS}"
}

params = {
    "user": {
        "first": first_name,
        "last": last_name,
        "email": email
    }
}
if email == check_email:
    response = requests.post(url=SHEETY_ENDPOINT, headers=header, json=params)
    print("User added")
else:
    print("Verification failed")