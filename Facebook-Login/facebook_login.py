# Automating facebook login

from selenium import webdriver
import time

url = "https://www.instagram.com/?hl=en"
browser = webdriver.Firefox()

browser.get(url)

time.sleep(3)
user_email = browser.find_element_by_name("username")
user_email.send_keys("your-email")

user_password = browser.find_element_by_name("password")
user_password.send_keys("your-password")
user_password.submit()

user_vertification = browser.find_element_by_name("verificationCode")
user_vertification.send_keys("152357")
user_vertification.submit()
