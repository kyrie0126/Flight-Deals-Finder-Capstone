import os
from dotenv import load_dotenv
from twilio.rest import Client
import requests
import smtplib


load_dotenv()

# Retrieve environmental variables
ACCT_SID = os.environ["TWILIO_ACCT_SID"]
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_NUM = os.environ["TWILIO_NUM"]
PERSONAL_NUM = os.environ["PERSONAL_NUM"]
SHEETY_ENDPOINT_USERS = os.environ["SHEETY_ENDPOINT_USERS"]
SHEETY_PASS_USERS = os.environ["SHEETY_BASE64_PASS_USERS"]
EMAIL_USER = os.environ["EMAIL_USER"]
EMAIL_PASS = os.environ["EMAIL_PASS"]

def text(item):
    client = Client(ACCT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=(f"Cheap flight to {item['cityTo']}!\n\n"
             f"${item['price']} for {item['nightsInDest']} days!\n\n"
             f"{item['deep_link']}"),
        from_=TWILIO_NUM,
        to=PERSONAL_NUM
    )
    print(message.status)


def send_emails(item):
    header = {
        "Authorization": f"Basic {SHEETY_PASS_USERS}"
    }
    response = requests.get(url=SHEETY_ENDPOINT_USERS, headers=header)
    result = response.json()
    emails = []
    for items in result['users']:
        emails.append(items['email'])
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=EMAIL_USER, password=EMAIL_PASS)
        connection.sendmail(
            from_addr=EMAIL_USER,
            to_addrs=emails,
            msg=(
                f"Subject:Cheap flight to {item['cityTo']}!\n\n"
                f"${item['price']} for {item['nightsInDest']} days!\n"
                f"{item['deep_link']}"
            )
        )

