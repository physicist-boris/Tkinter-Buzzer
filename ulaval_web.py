from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://secure.sas.ulaval.ca/rtpeps/Account/Login?ReturnUrl=%2Frtpeps%2FReservation")
assert "Se connecter - PEPS - Réservation de terrains" in driver.title
elem = driver.find_element_by_id("Email")
elem.clear()
elem.send_keys("elvisametolo@gmail.com")
elem = driver.find_element_by_id("Password")
elem.clear()
elem.send_keys("*********", Keys.ENTER)
time.sleep(5)

driver.find_elements_by_class_name("square")[0].click()




driver.refresh()
time.sleep(5)
assert "No results found." not in driver.page_source
driver.close()
