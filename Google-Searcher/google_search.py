# searching in google  using selenium in python
# the difference between "element" and "elements"
# element - string
# elements - lists

from selenium.webdriver import Firefox

# it provide keys in the keyboard like RETURN, ENTER, F1, ALT
from selenium.webdriver.common.keys import Keys
import time

browser = Firefox()

browser.get("https://www.google.com")

search = browser.find_element_by_name("q")
search.send_keys("Facebook login")
search.submit()

# below we are inputting 'ENTER' keyword
# search.send_keys(Keys.RETURN)
