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
from google.oauth2.service_account import Credentials
from bs4 import BeautifulSoup
import pickle

# Configure options for Chrome
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-data-dir=User Data")  
chrome_options.add_argument("profile-directory=Default")  

# Set the credentials file path
CREDENTIALS_FILE = "service_account.json"

# Ensure the credentials file exists
if not os.path.exists(CREDENTIALS_FILE):
    raise FileNotFoundError(f"Google credentials file '{CREDENTIALS_FILE}' not found. Ensure it's present in the repository.")

# Authenticate with Google Sheets API
with open(CREDENTIALS_FILE, "r") as file:
    credentials_json = json.load(file)
    
credentials = Credentials.from_service_account_info(json.loads(credentials_json))
gc = gspread.authorize(credentials)

# Open Google Sheets
open_sheet = gc.open('PD')
open_sheet1 = gc.open('Tradingview Data Reel Experimental December')
sh = open_sheet.worksheet('Sheet27')
company_list = sh.col_values(33)
name_list = sh.col_values(1)
sh1 = open_sheet1.worksheet('Sheet1')

current_date = date.today().strftime("%m/%d/%Y")  # Get current date in MM/DD/YYYY format

# Set the checkpoint filename
checkpoint_file = "checkpoint_new1.txt"

# Read last successful iteration
if os.path.exists(checkpoint_file):
    with open(checkpoint_file, "r") as f:
        last_successful_iteration = int(f.read().strip())
else:
    last_successful_iteration = 1

# Iterate over the list of companies
for i, company in enumerate(company_list[last_successful_iteration:], last_successful_iteration):
    chrome_options.add_argument("--headless")  # Run headless Chrome
    if i > 1903:
        break  # Stop the loop at 1903

    name = name_list[i]

    # Set up the WebDriver
    driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(20)

    try:
        # Load TradingView page
        driver.get(company)
        time.sleep(1)  # Allow page to load

        wait = WebDriverWait(driver, 30)
        element1 = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div')))

        # Parse page source
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract data
        value_elements = soup.find_all("div", class_="valueValue-l31H9iuA apply-common-tooltip")
        values = [value.get_text().replace('−', '-').replace('∅', 'None') for value in value_elements]

        # Append row to Google Sheets
        row = [name] + [current_date] + values
        sh1.append_row(row, table_range='A1')

    except NoSuchElementException as e:
        print(f"Error processing {company}: {str(e)}")

    finally:
        driver.quit()

    # Update checkpoint
    with open(checkpoint_file, "w") as f:
        f.write(str(i))
