from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
driver.get("https://www.forbes.com/top-colleges/")

cinfo = []

driver.implicitly_wait(30)

for i in range(10):
    print(i)
    time.sleep(0.5)
    tables = driver.find_elements(By.CLASS_NAME, "ListTable_tableRow__P838D")
    for i, element in enumerate(tables):
        c = [i]
        information = element.find_elements(By.TAG_NAME, "td")
        for el in information:
            c.append(el.text)
        cinfo.append(c)
    button = driver.find_elements(By.CSS_SELECTOR, ".DUQ8wnnp.JULvqjXa.TVxEFOXb._1Dl6Y2Kb._7zkbhAtG")[-1]
    if button.is_enabled():
        button.click()

print(cinfo)

with open('collegeinfo.txt', 'w') as filehandle:
    json.dump(cinfo, filehandle)

driver.quit()
