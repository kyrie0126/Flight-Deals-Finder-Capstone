# Flight-Deals-Finder-Capstone

## Description
Automatically notify users of cheap flights around the world using email and SMS!

## Relevant API's
You must create free accounts with the following APIs:
* Google Sheet Data Management: [SHEETY API](https://sheety.co/)
* Kiwi Partners Flight Search: [KIWI API](https://partners.kiwi.com/)
* Twilio SMS Messaging: [Twilio API](https://www.twilio.com/docs/sms)

## Environmental Variables
Store API-related information as environmental variables (either .env file or to local system)
* SHEETY_ENDPOINT_PRICES=(str) *Sheety API endpoint for 'prices' sheet*
* SHEETY_BASE64_PASS_PRICES=(str) *Sheety API Basic encryption for 'prices' sheet*
* SHEETY_ENDPOINT_USERS=(str) *Sheety API endpoint for 'users' sheet*
* SHEETY_BASE64_PASS_USERS=(str) *Sheety API Basic encryption for 'users' sheet*
* TEQUILA_KEY=(str) *Tequila API key*
* TWILIO_ACCT_SID=(str) *Twilio account SID*
* TWILIO_AUTH_TOKEN=(str) *Twilio authentication token*
* TWILIO_NUM=(str) *Twilio generated number*
* PERSONAL_NUM=(str) *trusted Twilio recipient number(s)*
* EMAIL_USER=(str) *sender's email*
* EMAIL_PASS=(str) *app-specific password*

## Adding Users
Copy and paste the add_users.py file to a browser-based IDE such as [replit](https://replit.com/~).
