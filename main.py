from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import send_emails

# Retrieve data from Sheety
sheet = DataManager()
search = FlightSearch()
current_data = sheet.retrieve()

# Autofill missing iata codes
for row in current_data:
    if row["iataCode"] == "":
        try:
            code = search.get_iata_code(row["city"])
            row_id = row["id"]
            sheet.update_code(row_id, code)
        except IndexError:
            continue

# Text link if flights below my price criteria appear
for row in current_data:
    result = search.price_search(row["iataCode"])
    price = result["price"]
    if price < row["lowestPrice"]:
        send_emails(item=result)


