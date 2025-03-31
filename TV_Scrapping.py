import json
import os
import time
from datetime import date
import gspread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from google.oauth2.service_account import Credentials
from bs4 import BeautifulSoup

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")  # Run headless Chrome
chrome_options.add_argument("user-data-dir=User Data")  
chrome_options.add_argument("profile-directory=Default")  

# Load Google credentials
CREDENTIALS_FILE = "service_account.json"
if not os.path.exists(CREDENTIALS_FILE):
    raise FileNotFoundError(f"Google credentials file '{CREDENTIALS_FILE}' not found.")

with open(CREDENTIALS_FILE, "r") as file:
    credentials_json = json.load(file)

# Authenticate with Google Sheets API
credentials = Credentials.from_service_account_info(credentials_json)
gc = gspread.authorize(credentials)

# Open Google Sheets
gsheets = gc.open('PD')
gsheets1 = gc.open('Tradingview Data Reel Experimental December')
sheet = gsheets.worksheet('Sheet27')
company_list = sheet.col_values(33)
name_list = sheet.col_values(1)
sheet1 = gsheets1.worksheet('Sheet1')

current_date = date.today().strftime("%m/%d/%Y")
checkpoint_file = "checkpoint_new1.txt"

# Read last successful iteration
last_successful_iteration = 1
if os.path.exists(checkpoint_file):
    with open(checkpoint_file, "r") as f:
        last_successful_iteration = int(f.read().strip())

# Iterate over the list of companies
for i, company in enumerate(company_list[last_successful_iteration:], last_successful_iteration):
    if i > 1903:
        break
    
    name = name_list[i]
    driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=chrome_options)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(20)
    
    try:
        driver.get(company)
        time.sleep(1)
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[5]/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div')))
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        value_elements = soup.find_all("div", class_="valueValue-l31H9iuA apply-common-tooltip")
        values = [value.get_text().replace('−', '-').replace('∅', 'None') for value in value_elements]
        
        row = [name] + [current_date] + values
        sheet1.append_row(row, table_range='A1')
    
    except Exception as e:
        print(f"Error processing {company}: {str(e)}")
    
    finally:
        driver.quit()
    
    with open(checkpoint_file, "w") as f:
        f.write(str(i))
