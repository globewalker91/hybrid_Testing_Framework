# Restful Booker Automation (UI + API)

This project demonstrates **combined API + UI testing** using [Restful Booker](https://automationintesting.online).

### Features
- API test: Create a booking via REST API
- UI test: Verify booking appears in admin portal
- Visual test: Validate booking table with Applitools Eyes
- Reporting: Allure HTML reports
- CI: GitHub Actions integration

### Run tests
```bash
pip install -r requirements.txt
pytest --alluredir=reports

