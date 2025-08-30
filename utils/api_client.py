import requests

class BookingAPI:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def create_booking(self, firstname, lastname):
        url = f"{self.BASE_URL}/booking"
        payload = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": 120,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2025-08-20",
                "checkout": "2025-08-25"
            },
            "additionalneeds": "Breakfast"
        }
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()

