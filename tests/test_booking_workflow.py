import pytest, uuid
from utils.api_client import BookingAPI
from utils.driver_factory import get_driver
from pages.admin_page import AdminPage
from applitools.selenium import Eyes

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_booking_via_api_and_verify_in_ui(driver):
    # Step 1: API → create booking
    api = BookingAPI()
    firstname = f"Test{uuid.uuid4().hex[:5]}"
    lastname = "Walker"
    booking = api.create_booking(firstname, lastname)
    booking_id = booking["bookingid"]

    # Step 2: UI → login and verify
    page = AdminPage(driver)
    page.open("https://automationintesting.online/admin")
    page.login()
    assert page.is_booking_present(firstname, lastname)

    # Step 3: Applitools visual validation
    eyes = Eyes()
    eyes.api_key = "YOUR_API_KEY"  # ideally set via env var
    eyes.open(driver, "Restful Booker Project", "Booking Verification")
    eyes.check_window("Bookings Table")
    eyes.close()

#Step 4: Kick off CICD
