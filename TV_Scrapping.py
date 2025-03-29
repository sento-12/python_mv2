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
credentials = {
    "type": "service_account",
    "project_id": "newsscraper-367610",
    "private_key_id": "8e3313f883ed4e319db32e10826497fdddef52f5",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCq+F6SUwEqwmEj\nsssVMf9JyJSFNOTGqVMgKKjr2rzkQVz+O2HBIUq5JVSQVia8G8Uy7qyV5NR//Xeu\nHeQBechC+VHeODONUhwgLk81Lcs+0TWr3G4uyLqNw0cXx8Yx3R064YTbD8BP87Jf\nIaLZ3FYyXz0GbnGiU155Tbz/aK5JDYUpPlmE7dp+3RYF6yG4pQ2M35MnIPSOZUd9\nPnonM1S13fFh9kGj6JfaFSWT3bpYLjTm88m8Y2rBbFUoAGr0jc6Cp8MeWKx6kRva\nNQ0J1shO5VqagdEJn5ogDdcsOM94jbTL6PLDdhJICjhuRmzvkjHXjE3QfvVRjy/l\nPcIQj4OdAgMBAAECggEAJTvxlrLqjGYoUya3WT6Z/zbmd4sxLr3GG3kXbsQkwp4k\nkz6Z975ZIHDLlaKZjXqLzB+UKRHcoKIyLBKY6yRbU5CqPnflbEffVbfYKrf2LVBR\nPMRFH725+TE33Ks2k/n4iW//Z9jqlE75wAOajJFSmWZJ60pmx4gaCVd/i21AFar3\nkuqOnvLm1sIJI6CfgsoB0r4T0up1FyUxHBe/h4hegsYJvt1BP64YrLsPa3w70FpR\nBqe+3xnozPy6SbpRLRan8SX2tsO9haYYuPpl7W5df1etEQWCxhjHW7UM5Pa44OaE\nK7KUrzpKeo2bcXnaFHKe0yQqBjNL9HiGQe5bnEUUYQKBgQDedEHfadGv2I1pi7at\nUHITQzIUL9Cp/5ti6KQd266dCDOhNy/TW/4TuEmc2AlUv9b1H+aPbfYybt5AEdNM\n3CMmlUR1eG8JFsZkZMuZ2I8K15adHOWb+Dv+5b5l/eECoaxq8D1ab3B0DwqzBazW\nxo7SXbaWlrUUC0wWZ4+bkUT5PQKBgQDEwJj+JMlHJJ7ouhSLKShDYxmFPm9Vl1pG\nfVC1Ho74xomcSTHuCacvmx3GEzCmthA5QPSHbjxvYlxgQiQB9aQlSrwF6Y9lS+F0\nAy2W3u32Gua4a40r4M2iCzc9YXx10uVE4sp85xBhb1bKRyXiFD+TXq3z2AREzE4E\nx6JLM5eZ4QKBgQCLOMdhQ6DwJN+cBsy1e3tpgsx8xdAaFNby+BZ+eVa3AMMPSrKr\n3Q8O2G95sdtlJwspLmXlrjQ/LBP8lSthFwUIyLKnslALqC1R96NVDau4ZWTlv4gU\nLS+fP7oBqvp/4x89bk13o/cFK8TOdebOJEaOcggsBvYdLVTZUMcX3bsFIQKBgDQU\nEqr6i7hkDhfl4TgwjbLAkWm+a/PI2yFbXDiEvS1GR/hxO2EZdwJX2ZqrS65k9Ihj\nFBag7ChDbdYgy60lGuywCnK6LrWOTz/I85FCstP4rOdVuIlLuMJSm62Il0wMpZkF\nOrmy45gWw29JQ9LCr01Pu1WW8RJQzbngKaokHtWhAoGARDPEY2hI4G+gZxWZsRRx\nZC1VNN7s9i3GtH9Wd9Uu8l+SChyM/DlYSSVV8gB+u2Ej+39n0raocH5690ecxq3B\n6h4xJHucUnVtAgb3Q2sxR8gmRWHmL9uPs23icU2z848jXFm7yckG3bO7NWZVAAUY\nWWKZE+Hdfe3nUudeXxgMfQ8=\n-----END PRIVATE KEY-----\n",
    "client_email": "newsscraper@newsscraper-367610.iam.gserviceaccount.com",
    "client_id": "108256613622716515423",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/newsscraper%40newsscraper-367610.iam.gserviceaccount.com"
}

# Set up Google Sheets API client
gc = gspread.service_account_from_dict(credentials)
open_sheet = gc.open('PD')
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
