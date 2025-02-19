from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import json

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
collegedata = []
driver = webdriver.Chrome(options=options)
with open('collegeinfo.txt', 'r') as file:
    json_string = file.read()
    data = json.loads(json_string)
    collegedata = data

data = collegedata[0:10]

driver.implicitly_wait(30)

driver.get("https://en.wikipedia.org/wiki/University_of_Houston–Clear_Lake")
time.sleep(1)

for i in range(len(data)):
    if data[i][1] != "":
        searchbar = driver.find_elements(By.CLASS_NAME, "cdx-text-input__input")[0]
        searchbar.send_keys(data[i][2])
        button = driver.find_elements(By.XPATH, "//button[contains(text(), 'Search')]")[0]
        print(button)
        button.click()
        time.sleep(0.5)
        table = driver.find_elements(By.CSS_SELECTOR, ".infobox.vcard")[0]
        grids = table.find_elements(By.TAG_NAME, "tr")
        img = grids[0].find_element(By.TAG_NAME, "img")
        imgurl = 'https:' + img.get_attribute('src')
        img_data = requests.get(imgurl).content
        with open(f'${i}.jpg', 'wb') as handler:
            handler.write(img_data)

# print(collegedata)

driver.quit()