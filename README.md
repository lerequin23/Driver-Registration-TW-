# 🛵 Taiwan Driver's Licence — Quick Registration Bot

> Automates the scooter licence exam registration on the Taiwan DMV website in **2–10 seconds**, while everyone else is filling the form by hand.

 **Tech:** Python · Selenium

---

## What it does

Taiwan's DMV exam slots ([mvdis.gov.tw](https://www.mvdis.gov.tw/m3-emv-trn/exm/locations)) fill up extremely fast. This bot automates the entire registration flow so that by the time a human finishes typing their name, the slot is already booked.

**Full flow automated:**

1. Opens the DMV registration website
2. Selects the exam type — 普通重型機車 (regular heavy scooter)
3. Selects the region and specific test location (e.g. 士林監理站, Taipei)
4. Enters the desired exam date
5. Clicks search and selects the last available session
6. Clicks through the sign-up and terms agreement
7. Fills in all personal details — ID number, birthday, name, phone, email
8. Submits the registration

---

## Requirements

```bash
pip install selenium
```

You also need **ChromeDriver** matching your installed Chrome version:
- Download from: https://chromedriver.chromium.org/downloads
- Or install automatically via: `pip install webdriver-manager`

---

## Configuration

Before running, edit the top of the script to set your target location and date:

```python
# Location options (uncomment the one you want)
taipei  = "臺北市區監理所（含金門馬祖）"
shilin  = "士林監理站(臺北市士林區承德路5段80號)"
chiayi  = "嘉義區監理所（雲嘉南）"
taichung = "臺中區監理所（中彰投）"

# Date — Taiwan calendar year (民國), format: YYYMMDD
time_test = "1150115"  # = 2026/01/15
```

Then fill in the user details at the bottom:

```python
user1 = {
    'name':          'your name',
    'Phone number':  'your phone',
    'id_num_arc':    'your ID / ARC number',
    'birth_d_Taiwan year': 'YYYMMDD',
    'email':         'your email'
}
```

---

## Usage

```bash
python Drivers_license_quick_registration.py
```

A Chrome window will open and complete the registration automatically. Do not interact with the browser while it runs.

> **Note:** The script includes a `time.sleep(10)` after loading the page to allow the site to fully render before interacting. This is intentional.

---

## Supported locations

| Region | Location variable |
|--------|------------------|
| Taipei | `taipei` |
| Shilin (Taipei) | `shilin` |
| Chiayi | `chiayi` |
| Taichung | `taichung` |

To add more locations, copy the visible text from the dropdown on the website and add it as a new variable.

---

## Disclaimer

This bot was built for personal use to register for a legitimate driving licence exam. It does not bypass any security measures or CAPTCHAs — it simply fills the form faster than doing it by hand.

---

## Tech Stack

- **Python 3**
- **Selenium WebDriver** — browser automation
- **WebDriverWait / ExpectedConditions** — smart waiting instead of fixed sleeps
- **Select** — for interacting with dropdown menus
