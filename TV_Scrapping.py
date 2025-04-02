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

# # Load Google credentials
# credentials = {
#   "type": "service_account",
#   "project_id": "newsscraper-367610",
#   "private_key_id": "8d6a8ea0eea08ebf69ff85113e50e08fcd7803d4",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCqyMaexIV33MaL\nWYO151F7K9gcC4DWAouCW42m39ni0xMsfKEcHgfEI+I5tBIbu+IX3CVACzYVqRQM\nprxB1huJlF3mEMN3e29dAbBtzvTHsWD99IQhvMyvRyhx4VgSaGtTs9ymWEFYFTMd\nWWeI5tz2oJ0JeWd0I+Gz+9UVqR+dZ1zuANVkCH35d8utuUE2M6MExOdUeqa8fAm5\nt6bU5KfUTIUJbDCjYBrRzLz+kzFcH8iq1ZuXIXFemrQq6vWFb9iT6ETRZLh4bsCq\nxuIBvrU1z3VtNlm82pcrJN1X1BiBIUQR1DJgTpKwBs0KQkBUEHa6OqdDL8aXFKKZ\nGFbHsnwhAgMBAAECggEAAavfGL7s3PZPyZ2VxsYVo65TSjv5Fe8WsS8G8P0EF36Q\nE5mBJKKtGgftXvnyiuuw6+GbSjgJ3pal4/VORpkrMhKeBCJCHXVbasY5VSvHNLyZ\nScb2s5NSz/zS6iFl0KFNupcaJ9UZh5yGgGkndJ0oyK+b9dOmtenje7TRWinKbcqI\n8n0xsuc8mRJAZF9l1JuSXLUOAPj5sHeHRBFL72JfuRqgEvxdjQOnFpv/xBUlVfCz\niwIIiHcUVrK6Ujrs0hEolrFto4KMvvyxIMuH92VEBCmxHvkbaQYG6P5iDxenyWjh\niMJxmWTYqDZhbc9nXXXoG+ipml3Jq1FgJzqyhvTlCQKBgQDFgn07ozGKBQ0o/j60\nP+Mr3yfH7UNYaWnIu3bWeRQAPJlBSSgQqutH4wHc4mNx7aFpqV6sa/rViyEedxWm\nYj1K77v+VjXtFC/IDcIQZieZD64YGT4ne/RycH2Csv3V24ZFxNLtA45Kz3SPTlFq\nzkhU7BKwc+MaxFJL4RrayljiKQKBgQDdXDDA4Vh5ZRWuwoWYfDc7UFruMq/umm5Q\nH06iFfEKyc2jAICUkXI9DMsGZSo+BnPM75KO+c/S2Ml0lyV3dDtSek5ejd4EAVVT\nuQt/9mb/o4cVHf6HhKDrMcfQM36lm7WolCkxEiIZpy3zN8qlYVnw4lqmhU1bATED\nNMgldsU5OQKBgQDBfIXGiKadOTmdMQSoe/XGIsTL3Kke0ZWp6cwPa2mmmbbg+BPh\n0C7Rq5dFlhopn8uCwUNX0ihWTgfR2oNBDfhRku0tybLmX+I3LxMwEYM1NOEuBnyX\nHZ1pBr5N7Z8xg+7UJm8jdVpN+1GKmgS0hwTg/KuKZNzUegLNBubR82yDkQKBgQCk\n7Fb2ne6JI6Mv/YYDwih0bL4S0nj50N13nJu9b5OTch9f3rPt/R+cFLf/H8iFRdFp\nUuVi2QTaFuKhlys3AMZiAPX6xMAxQ70LD8ddo3vB41h1h09oMIykLwasPHGTeZuy\n6hB2mwgFDOXTXDIDXbDhJAReJNspfo3B0cV9BCyVIQKBgQCP8OIWea9v/BPzQS1a\ntytBPxpXx00GaRXECLaPQHMzxuFP/hfnvBEANJ7rfu5oNd+6Uk2cPrXi9vMATUMo\n5BIQtK1BakxzuAO8d9EOWerpohsA+oaucwEDr7lRMe5OEk8tFZKyXiC6Un++An4g\nnDB7NfKQbPtlqEL7FDmq345/Iw==\n-----END PRIVATE KEY-----\n",
#   "client_email": "newsscraper@newsscraper-367610.iam.gserviceaccount.com",
#   "client_id": "108256613622716515423",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/newsscraper%40newsscraper-367610.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }

# Use local file instead of environment variable
CREDENTIALS_FILE = "service_account.json"

if not os.path.exists(CREDENTIALS_FILE):
    raise ValueError("Google credentials file not found!")

with open(CREDENTIALS_FILE, "r") as f:
    credentials = json.load(f)

gc = gspread.service_account_from_dict(credentials)



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
    driver = webdriver.Chrome(service=Service('chromedriver'), options=chrome_options)
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
