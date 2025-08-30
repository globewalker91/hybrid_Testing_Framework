from selenium.webdriver.common.by import By

class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def login(self):
        # Default creds for demo site
        self.driver.find_element(By.ID, "username").send_keys("admin")
        self.driver.find_element(By.ID, "password").send_keys("password")
        self.driver.find_element(By.ID, "doLogin").click()

    def is_booking_present(self, firstname, lastname):
        bookings = self.driver.find_elements(By.CSS_SELECTOR, ".row .col-sm-3 p")
        return any(firstname in b.text or lastname in b.text for b in bookings)

