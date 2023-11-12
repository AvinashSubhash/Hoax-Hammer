from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriveManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def generate_random_mobile_number():
    # The dance of digits begins
    mobile_number = '9'  # Start with a valid Indian mobile number prefix
    
    # Generate the rest of the digits
    for _ in range(9):
        digit = random.randint(0, 9)
        mobile_number += str(digit)
    
    return mobile_number

# Initialize the Selenium webdriver (you need to specify the path to your webdriver executable)

s = Service(r"/home/kingaiva/chromedriver")
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080');
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(service=s,options=options)

# Navigate to the webpage

while True:
    driver.get('https://fbj.74d.myftpupload.com/')
    # Wait for the page to load
    time.sleep(2)
    # Find the Upi Payment Option dropdown element and select an option
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    upi_payment_option = Select(driver.find_element(By.NAME,'UpiPaymentOption'))
    payment_option_list= ['PhonePe','Google Pay','Paytm','Ola Money','Mobikwik','BHIM','Other']
    payment_option = random.choice(payment_option_list)
    upi_payment_option.select_by_visible_text(payment_option)


    # Find the Bank Name dropdown element and select a bank
    bank_name = Select(driver.find_element(By.NAME,'BankMane'))
    bank_list = ['Punjab National Bank', 'State Bank of India', 'Union Bank of India', 'UCO Bank', 'Indian Overseas Bank', 'Punjab & Sind Bank', 'Indian Bank', 'Central Bank of India', 'Canara Bank', 'Bank of Maharashtra', 'Bank of India', 'Bank of Baroda', 'Axis Bank Ltd.', 'Bandhan Bank Ltd.', 'HDFC Bank Ltd', 'ICICI Bank Ltd.', 'Induslnd Bank Ltd', 'IDFC First Bank Ltd.', 'RBL Bank Ltd.', 'india Post Payments Bank', 'Fino Payments Bank', 'Paytm Payments Bank', 'Telangana Grameena Bank', 'Uttar Bihar Gramin Bank', 'Dhanlaxmi Bank Ltd.', 'ICICI Bank Ltd.', 'Induslnd Bank Ltd', 'IDFC First Bank Ltd.', 'Jammu & Kashmir Bank', 'Karnataka Bank Ltd.', 'RBL Bank Ltd.', 'Tamilnad Mercantile Bank', 'YES Bank Ltd.', 'IDBI Bank Ltd.', 'Other']

    bank_option = random.choice(bank_list)
    bank_name.select_by_visible_text(bank_option)
    mobile_number = driver.find_element(By.NAME,'number-15')
    random_mobile_number = generate_random_mobile_number()
    mobile_number.send_keys(random_mobile_number)
    amount = driver.find_element(By.NAME,'Amount')
    amount.send_keys(str(random.randint(1, 5)))
    upin = driver.find_element(By.NAME,'Upin')
    upin.send_keys(str(random.randint(1000,999999)))
    submit_button = driver.find_element(By.CLASS_NAME,'wpcf7-submit')
    submit_button.click()
    time.sleep(5)
    result = driver.find_element(By.CLASS_NAME,'wpcf7-response-output').text
    os.system('echo "'+time.ctime(time.time())+' '+result+'" > /home/kingaiva/.loginfo')
    #print(result)
driver.quit()