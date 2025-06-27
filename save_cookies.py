from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

input("✅ Log in manually and reach the Instagram homepage. THEN press Enter here to save cookies...")

# Take screenshot to confirm
driver.save_screenshot("login_status.png")

# Save cookies
with open("insta_cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Cookies saved successfully.")
driver.quit()
