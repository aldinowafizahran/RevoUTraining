from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path="/usr/local/bin/firefoxdriver")
with webdriver.Firefox(service=service) as driver:
    driver.get("https://coderbyte.com")
    my_current_url = driver.current_url
    print(my_current_url)