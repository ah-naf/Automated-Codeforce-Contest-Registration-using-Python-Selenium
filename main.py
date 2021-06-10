from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


USERNAME = input("Enter your Handle/Email: ")
PASSWORD = input("Enter your Password: ")

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

contest_link = driver.find_elements_by_link_text('Register »')

for contest in contest_link:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT , 'Register »')))

    element.click()
    time.sleep(2)
    submit = driver.find_element_by_css_selector('input.submit')
    CurrentUrl = driver.current_url
    submit.click()
    time.sleep(2)

    if CurrentUrl == driver.current_url:
        driver.back()
        continue
    else: continue

driver.quit()
