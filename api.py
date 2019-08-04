from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#search for the name shanjai raj
#only then it will perform what it it should
search = input("What do you want to search ? - ")
driver = webdriver.Firefox()
driver.get("https://www.google.com")
driver.find_element_by_name("q").send_keys(search)
driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div/div[3]/center/input[1]").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/div/div[1]/div/div/div[1]/div/div[2]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/a/h3").click()
#driver.quit()
