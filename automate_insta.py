import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Step 1: Open Instagram and load cookies
driver.get("https://www.instagram.com/")
time.sleep(5)

with open("insta_cookies.pkl", "rb") as f:
    cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)

driver.get("https://www.instagram.com/")
time.sleep(5)
print("✅ Logged in using saved cookies.")

wait = WebDriverWait(driver, 10)

# Step 2: Search for the cbitosc profile
try:
    search_input = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
    )
    search_input.clear()
    search_input.send_keys("cbitosc")
    time.sleep(2)
    search_input.send_keys(Keys.RETURN)
    time.sleep(2)
    search_input.send_keys(Keys.RETURN)
    print("🔍 Navigated to cbitosc profile.")
    time.sleep(5)
except Exception as e:
    print("❌ Could not search for profile:", e)
    driver.save_screenshot("search_error.png")
    driver.quit()
    exit()

# Step 3: Follow the user if not already following
try:
    follow_button = driver.find_element(By.XPATH, "//button[text()='Follow']")
    follow_button.click()
    print("✅ Followed the account.")
except:
    print("ℹ️ Already followed or Follow button not found.")

# Step 4: Extract profile info
profile = {}
try:
    stats = driver.find_elements(By.XPATH, "//header//ul/li")

    profile["Posts"] = stats[0].text
    profile["Followers"] = stats[1].text
    profile["Following"] = stats[2].text
except:
    print("⚠️ Could not fetch stats.")
    profile["Posts"] = profile["Followers"] = profile["Following"] = "N/A"

try:
    bio = driver.find_element(By.XPATH, "//section/main/div/header/section/div").text
    profile["Bio"] = bio
except:
    profile["Bio"] = "N/A"

with open("cbitosc_profile.txt", "w", encoding="utf-8") as f:
    for key, value in profile.items():
        f.write(f"{key}: {value}\n")

print("📄 Profile info saved to cbitosc_profile.txt")
driver.quit()
