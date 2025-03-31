from selenium import webdriver
import time
from datetime import date
import gspread
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json

from bs4 import BeautifulSoup
import pickle

# Configure options for Chrome
chrome_options = Options()
# chrome_options.add_argument("--remote-debugging-port=9222")  # Change this port for each instance
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument(
    "user-data-dir=User Data")  # Main user data directory
chrome_options.add_argument("profile-directory=Default")  # Specify the profile if necessary

# Authenticate with Google Sheets API
credentials_json = os.getenv("GOOGLE_CREDENTIALS")
if credentials_json:
    credentials = json.loads(credentials_json)
    gc = gspread.service_account_from_dict(credentials)
    open_sheet = gc.open('PD')
else:
    raise ValueError("Google credentials not found in environment variables")
# Set up Google Sheets API client
# credentials = json.loads(credentials_json)
# gc = gspread.service_account_from_dict(credentials)
# open_sheet = gc.open('PD')
open_sheet1 = gc.open('Tradingview Data Reel Experimental December')
sh = open_sheet.worksheet('Sheet27')
company_list = sh.col_values(33)
name_list = sh.col_values(1)
sh1 = open_sheet1.worksheet('Sheet1')

current_date = date.today().strftime("%m/%d/%Y")  # Get current date in DD/MM/YYYY format

# Set the checkpoint filename and path
checkpoint_file = "checkpoint_new1.txt"

# If the checkpoint file exists, read the last successful iteration number from it
if os.path.exists(checkpoint_file):
    with open(checkpoint_file, "r") as f:
        last_successful_iteration = int(f.read().strip())
        print(last_successful_iteration)
else:
    last_successful_iteration = 1

# Iterate over the list of companies
for i, company in enumerate(company_list[last_successful_iteration:], last_successful_iteration):
    chrome_options.add_argument("--headless")
    if i > 1903:
        break  # Stop the loop when the iteration number reaches 325

    name = name_list[i]

    # Set up the webdriver with existing session
    driver = webdriver.Chrome(
        service=Service('chromedriver.exe'),
        options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(20)

    try:
        # Load the webpage for the company (TradingView link)
        driver.get(company)
        time.sleep(1)  # Wait for a moment to let the page load

        wait = WebDriverWait(driver, 30)

        # Wait for the specific element to be visible (adjust XPath as needed)
        element1 = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div')))

        # Get the page source after data is loaded
        page_source = driver.page_source

        # Pass the page source to Beautiful Soup for parsing
        soup = BeautifulSoup(page_source, "html.parser")

        # Extract data using CSS selectors or other methods
        value_elements = soup.find_all("div", class_="valueValue-l31H9iuA apply-common-tooltip")

        # Initialize empty lists to store the values
        values = []

        # Loop through the elements and get their text values
        for value_element in value_elements:
            value_text = value_element.get_text()

            # Preprocess the value_text to remove non-numeric characters and handle 'K' and 'M'
            cleaned_value = value_text.replace('−', '-').replace('∅', 'None')
            values.append(cleaned_value)

        # Convert values to strings for Google Sheets compatibility
        values = [str(value) for value in values]
        row = [name] + [current_date] + values

        # Append row to Google Sheets
        sh1.append_row(row, table_range='A1')

    except NoSuchElementException as e:
        print(f"Encountered an error while processing {company}: {str(e)}")

    finally:
        # Close the Selenium WebDriver after each iteration
        driver.quit()

    # Update the last successful iteration number in the checkpoint file
    with open(checkpoint_file, "w") as f:
        f.write(str(i))
