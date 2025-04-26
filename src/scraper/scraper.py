from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import time 
from extractor import extract_and_save_coffee_data
load_dotenv()

# Load environment variables from .env file
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Load Chrome WebDriver
driver = webdriver.Chrome()
time.sleep(2)

# Open the login page
driver.get('https://database.coffeeinstitute.org/login')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))

#Enter email and password
username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys(email)
password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys(password)
time.sleep(2)
login_button = driver.find_element(By.CLASS_NAME, 'submit')
login_button.click()

#Wait for the page to load
time.sleep(10)

# find the coffee tab and click it
coffee_tab = driver.find_element(By.CLASS_NAME, 'coffees')
coffee_tab.click()

# load the arabica coffee table
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Arabica Coffees'))).click()
time.sleep(30)


# loop through the pages and open each coffee link in a new tab
while True:
    links = driver.find_elements(By.XPATH, "//table[@data-table='coffees']//a[contains(@href, '/coffee/')]")
    
    for link in links:

        link.send_keys(Keys.COMMAND + Keys.RETURN) 
        driver.switch_to.window(driver.window_handles[-1]) 
        time.sleep(5)
        extract_and_save_coffee_data(driver)
        driver.close() 
        driver.switch_to.window(driver.window_handles[0]) 

    try:
        next_button = driver.find_element(By.LINK_TEXT, "Next")
        if "disabled" in next_button.get_attribute("class"):
            print("Reached last page.")
            break 
        else:
            next_button.click()
            time.sleep(5) 
    except:
        print("Next button not found.")
        break





