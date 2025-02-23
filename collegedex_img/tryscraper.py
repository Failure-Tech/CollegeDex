# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests
# import time
# import json

# options = webdriver.ChromeOptions()
# options.page_load_strategy = 'normal'
# collegedata = []
# driver = webdriver.Chrome(options=options)
# with open('./collegedex_img/collegeinfo.txt', 'r') as file:
#     json_string = file.read()
#     data = json.loads(json_string)
#     collegedata = data

# driver.implicitly_wait(7200)
# driver.maximize_window()
# driver.get("https://en.wikipedia.org/wiki/University_of_Houston–Clear_Lake")
# time.sleep(1.5)

# for i in range(len(collegedata)):
#     if data[i][1] != "":
#         searchbar = driver.find_elements(By.CLASS_NAME, "cdx-text-input__input")[0]
#         searchbar.send_keys(data[i][2])
#         time.sleep(0.5)
#         try:
#             listitem = driver.find_elements(By.CLASS_NAME, "cdx-menu__listbox")[0]
#             it = listitem.find_elements(By.TAG_NAME, "li")[0]
#             a = it.find_element(By.TAG_NAME, "a")
#             a.click()
#             time.sleep(0.5)
#             table = driver.find_elements(By.CSS_SELECTOR, ".infobox.vcard")[0]
#             grids = table.find_elements(By.CLASS_NAME, "infobox-image")[0]
#             img = grids.find_element(By.TAG_NAME, "img")
#             imgurl = img.get_attribute('src')
#             spl = imgurl.split('.')[-1]
#             img_data = requests.get(imgurl).content
#             with open(f'./work/{data[i][1]}.{spl}', 'wb') as handler:
#                 handler.write(img_data)
#             time.sleep(1)
#         except:
#             time.sleep(1)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import json
import urllib.parse

options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
collegedata = []
driver = webdriver.Chrome(options=options)

# Load college information
with open('collegeinfo.txt', 'r', encoding='utf-8') as file:
    json_string = file.read()
    data = json.loads(json_string)
    collegedata = data

# Set implicit wait and maximize window
driver.implicitly_wait(10)
driver.maximize_window()

for i in range(len(collegedata)):
    if data[i][1] != "":
        # Construct the Wikipedia URL for each university
        university_name = data[i][2]
        url_name = urllib.parse.quote(university_name.replace(" ", "_"))  # encode university name
        wiki_url = f"https://en.wikipedia.org/wiki/{url_name}"
        
        # Navigate to the constructed URL
        driver.get(wiki_url)
        time.sleep(1.5)

        try:
            # Locate the infobox and image
            table = driver.find_elements(By.CSS_SELECTOR, ".infobox.vcard")[0]
            grids = table.find_elements(By.CLASS_NAME, "infobox-image")[0]
            img = grids.find_element(By.TAG_NAME, "img")
            imgurl = img.get_attribute('src')

            # Handle dynamic image resolution
            spl = imgurl.split('.')[-1]
            img_data = requests.get(imgurl).content

            # Save the image locally
            with open(f'./work/{data[i][1]}.{spl}', 'wb') as handler:
                handler.write(img_data)

            time.sleep(1)
        except Exception as e:
            print(f"Error processing {university_name}: {e}")
            time.sleep(1)

# Close the browser
driver.quit()