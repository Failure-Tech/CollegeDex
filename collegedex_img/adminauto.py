# import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.webdriver.common.keys import Keys

# # Initialize the webdriver with Chrome options
# options = webdriver.ChromeOptions()
# options.page_load_strategy = 'normal'
# driver = webdriver.Chrome(options=options)

# def wait_and_send_keys(driver, by, value, keys, wait_time=30):
#     """Wait for an element to be clickable and send keys."""
#     WebDriverWait(driver, wait_time).until(
#         EC.element_to_be_clickable((by, value))
#     ).send_keys(keys)

# def perform_add_ball_action():
#     """Click on the 'Add ball' button/link."""
#     try:
#         add_ball_link = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.object-tools a.addlink"))
#         )
#         print("Add ball link found, clicking now...")
#         add_ball_link.click()
#     except Exception as e:
#         print("Failed to click on 'Add ball':", e)

# # def select_regime(driver, regime_value="Leeching"):
# #     """Handle Select2 dropdown selection for regime using Enter key."""
# #     try:
# #         # First click the Select2 selection span to open the dropdown
# #         select2_selection = WebDriverWait(driver, 10).until(
# #             EC.element_to_be_clickable((By.CLASS_NAME, "select2-selection"))
# #         )
# #         select2_selection.click()
# #         time.sleep(1)  # Wait for dropdown to open
        
# #         # Now find and interact with the search field that appears
# #         search_field = WebDriverWait(driver, 10).until(
# #             EC.presence_of_element_located((By.CLASS_NAME, "select2-search__field"))
# #         )
# #         search_field.send_keys(regime_value)
# #         time.sleep(1)  # Wait for search results
# #         search_field.send_keys(Keys.ENTER)
        
# #         print(f"Successfully selected regime: {regime_value}")
# #         return True
# #     except Exception as e:
# #         print(f"Error selecting regime: {e}")
# #         return False

# def select_regime(driver, regime_value="Leeching"):
#     """Handle Select2 dropdown selection for regime using Enter key."""
#     try:
#         # Find all Select2 selections and click the second one
#         select2_selections = WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.CLASS_NAME, "select2-selection"))
#         )
#         if len(select2_selections) >= 2:
#             select2_selections[1].click()  # Click the second Select2 dropdown
#         else:
#             print("Could not find second Select2 dropdown")
#             return False
            
#         time.sleep(1)  # Wait for dropdown to open
        
#         # Now find and interact with the search field that appears
#         search_field = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "select2-search__field"))
#         )
#         search_field.send_keys(regime_value)
#         time.sleep(1)  # Wait for search results
#         search_field.send_keys(Keys.ENTER)
        
#         print(f"Successfully selected regime: {regime_value}")
#         return True
#     except Exception as e:
#         print(f"Error selecting regime: {e}")
#         return False

# def fill_form_from_data(entry):
#     """Fills the form fields with data from a single entry."""
#     time.sleep(2)  # Ensure all preconditions are met

#     wait_and_send_keys(driver, By.ID, "id_country", entry[2])
#     driver.find_element(By.ID, "id_health").send_keys(str(int(entry[-1]["health"])))
#     driver.find_element(By.ID, "id_attack").send_keys(str(int(entry[-1]["attack"])))
#     driver.find_element(By.ID, "id_rarity").send_keys(entry[1])  # Send rank from the entry
#     driver.find_element(By.ID, "id_emoji_id").send_keys("1343071816004141137")

#     # Handle regime selection with retry logic
#     max_retries = 3
#     for attempt in range(max_retries):
#         if select_regime(driver):
#             break
#         else:
#             print(f"Attempt {attempt + 1} failed, retrying...")
#             time.sleep(2)
    
#     time.sleep(2)
    
#     # Upload files
#     image_path = r"C:\Users\korra\OneDrive\Desktop\collegedex\CollegeDex\collegedex_img\images\8.png"
#     driver.find_element(By.ID, "id_wild_card").send_keys(image_path)
#     driver.find_element(By.ID, "id_collection_card").send_keys(image_path)
#     time.sleep(2)

#     driver.find_element(By.ID, "id_credits").send_keys("Stonkpotato and Student")
#     driver.find_element(By.ID, "id_capacity_name").send_keys("Moneyball")
#     driver.find_element(By.ID, "id_capacity_description").send_keys("Has infinite money to spend on any types of things")

#     # Click on the "Save and add another" button
#     save_add_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//input[@value='Save and add another']"))
#     )
#     save_add_button.click()
#     time.sleep(2)

# try:
#     # Load updated college data
#     with open('collegeinfo_updated.txt', 'r', encoding='utf-8') as file:
#         collegedata = json.load(file)

#     # Navigate to the website
#     driver.get("http://localhost:8000/")
#     time.sleep(5)  # Allow page to load
    
#     # Ensure the "Add ball" action is performed before filling the form
#     perform_add_ball_action()
    
#     # Directly fill the form for the first entry
#     if collegedata:
#         fill_form_from_data(collegedata[0])

# finally:
#     # Close the driver after operations
#     driver.quit()

import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

# Initialize the webdriver with Chrome options
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

def wait_and_send_keys(driver, by, value, keys, wait_time=30):
    """Wait for an element to be clickable and send keys."""
    WebDriverWait(driver, wait_time).until(
        EC.element_to_be_clickable((by, value))
    ).send_keys(keys)

def perform_add_ball_action():
    """Click on the 'Add ball' button/link."""
    try:
        add_ball_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.object-tools a.addlink"))
        )
        print("Add ball link found, clicking now...")
        add_ball_link.click()
    except Exception as e:
        print("Failed to click on 'Add ball':", e)

def select_regime(driver, regime_value="Leeching"):
    """Handle Select2 dropdown selection for regime using Enter key."""
    try:
        # Find all Select2 selections and click the second one
        select2_selections = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "select2-selection"))
        )
        if len(select2_selections) >= 2:
            select2_selections[1].click()  # Click the second Select2 dropdown
        else:
            print("Could not find second Select2 dropdown")
            return False
            
        time.sleep(1)  # Wait for the dropdown to open
        
        # Now find and interact with the search field that appears
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "select2-search__field"))
        )
        search_field.send_keys(regime_value)
        time.sleep(1)  # Wait for search results
        search_field.send_keys(Keys.ENTER)
        
        print(f"Successfully selected regime: {regime_value}")
        return True
    except Exception as e:
        print(f"Error selecting regime: {e}")
        return False

def fill_form_from_data(entry, emoji_id):
    """Fills the form fields with data from a single entry."""
    time.sleep(2)  # Ensure all preconditions are met

    wait_and_send_keys(driver, By.ID, "id_country", entry[2])
    driver.find_element(By.ID, "id_health").send_keys(str(int(entry[-1]["health"])))
    driver.find_element(By.ID, "id_attack").send_keys(str(int(entry[-1]["attack"])))
    driver.find_element(By.ID, "id_rarity").send_keys(entry[1])  # Send rank from the entry
    driver.find_element(By.ID, "id_emoji_id").send_keys(emoji_id)

    # Handle regime selection with retry logic
    max_retries = 3
    for attempt in range(max_retries):
        if select_regime(driver):
            break
        else:
            print(f"Attempt {attempt + 1} failed, retrying...")
            time.sleep(2)
    
    time.sleep(2)
    
    # Upload files
    image_file = f"{image_counter}.png"
    image_path = os.path.join(images_dir, image_file)
    
    if os.path.exists(image_path):
        driver.find_element(By.ID, "id_wild_card").send_keys(image_path)
        driver.find_element(By.ID, "id_collection_card").send_keys(image_path)
    else:
        print(f"Image file not found: {image_file}")
        
    time.sleep(2)
    
    driver.find_element(By.ID, "id_credits").send_keys("Stonkpotato and Student")
    driver.find_element(By.ID, "id_capacity_name").send_keys("Moneyball")
    driver.find_element(By.ID, "id_capacity_description").send_keys("Has infinite money to spend on any types of things")

    # Click on the "Save and add another" button
    save_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Save and add another']"))
    )
    save_add_button.click()
    time.sleep(2)

# Prepare images directory path
images_dir = r"C:\Users\korra\OneDrive\Desktop\collegedex\CollegeDex\collegedex_img\images"

try:
    # Load updated college data
    with open('collegeinfo_updated.txt', 'r', encoding='utf-8') as file:
        collegedata = json.load(file)

    # Read emoji IDs while eliminating duplicates
    with open('emojids.txt', 'r') as file:
        emoji_ids = list(dict.fromkeys(line.strip() for line in file if line.strip()))

    # Starting image counter
    image_counter = 1

    # Navigate to the website
    driver.get("http://localhost:8000/")
    time.sleep(5)  # Allow page to load

    # Fill forms using each unique emoji ID
    for index, emoji_id in enumerate(emoji_ids):
        if image_counter > len(collegedata):
            break

        perform_add_ball_action()
        fill_form_from_data(collegedata[index], emoji_id)
        image_counter += 1

finally:
    # Close the driver after operations
    driver.quit()