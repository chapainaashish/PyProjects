

# automating browser to login facebook account
# Author: Aashish Sharma

from selenium import webdriver
import time


url = """https://www.instagram.com/p/CZ3AiSntkjO/?utm_source=ig_web_copy_link"""
browser = webdriver.Firefox()

browser.get(url)

time.sleep(3)


browser.find_element_by_class_name("fr66n").click()
