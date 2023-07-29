from selenium import webdriver
driver = webdriver.Firefox()

driver.get("https://coderbyte.com")
url = driver.current_url
driver.close()