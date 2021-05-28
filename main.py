from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


USERNAME = input("Enter your Codeforce Handle/Email: ")
PASSWORD = input("Enter your password: ")

path = "chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)

driver.get("https://www.codeforces.com")

enter_button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/a[1]')
enter_button.click()

time.sleep(3)

handle = driver.find_element_by_id("handleOrEmail")
handle.send_keys(USERNAME)
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(PASSWORD)
login_button = driver.find_element_by_xpath('//*[@id="enterForm"]/table/tbody/tr[4]/td/div[1]/input')
login_button.click()

time.sleep(5)
contest_menu = driver.find_element_by_xpath('//*[@id="body"]/div[3]/div[5]/ul/li[3]/a')
contest_menu.click()

# //*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr[2]/td[6]/a[1]
for i in range(2,5):
    time.sleep(5)
    check = True
    try:
        path = f'//*[@id="pageContent"]/div[1]/div[1]/div[6]/table/tbody/tr[{i}]/td[6]/a[1]'
        register_menu = driver.find_element_by_xpath(path)
        register_menu.click()

        time.sleep(3)

        register_button = driver.find_element_by_xpath('//*[@id="pageContent"]/form/table/tbody/tr[3]/td/div/input')

    except NoSuchElementException:
        driver.back()
        continue
    else:
        #page_content = driver.find_element_by_css_selector("#pageContent h2")
        #print(page_content.text)
        register_button.click()
        continue

driver.quit()
