import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the webdriver with Chrome options
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

def upload_emoji(image_file, emoji_name):
    """Uploads an emoji, updates its name, and ensures the ID is captured."""
    max_retries = 5
    retries = 0
    success = False
    
    while not success and retries < max_retries:
        try:
            # Click the upload button
            upload_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "uploadButtonEnabled-3-zMe9"))
            )
            upload_button.click()

            # Locate the file input element and upload file
            file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
            file_input.send_keys(image_file)

            # Wait for the emoji name input to be interactable
            emoji_name_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "inputMini-Un2tP4"))
            )
            emoji_name_input.clear()
            emoji_name_input.send_keys(emoji_name)

            # Wait for emoji ID to appear and capture it
            emoji_id_span = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "cellId--lByq3"))
            )
            emoji_id = emoji_id_span.text.strip()

            print(f"Uploaded emoji for {emoji_name}, ID: {emoji_id}")

            # Save only the emoji id to a file
            with open("emoji_ids.txt", "a") as file:
                file.write(f"{emoji_id}\n")

            success = True

        except Exception as e:
            retries += 1
            print(f"Error uploading {emoji_name} (attempt {retries}): {e}")
            if retries < max_retries:
                print("Retrying...")
            time.sleep(2)  # Wait before retrying

try:
    # Navigate to the website
    driver.get("https://discord.com/developers/applications/1341164828730986666/emojis")
    time.sleep(30)  # Allow page to load

    # Load updated college data
    with open('collegeinfo_updated.txt', 'r', encoding='utf-8') as file:
        collegedata = json.load(file)

    # Prepare images directory path
    images_dir = r"C:\Users\korra\OneDrive\Desktop\collegedex\CollegeDex\collegedex_img\images"
    
    # Ensure all images are processed in order
    images = sorted(os.listdir(images_dir), key=lambda x: int(x.split('.')[0]))

    for index, image_number in enumerate(images):
        image_file = os.path.join(images_dir, image_number)
        
        # Assume the emoji name corresponds to entry[2] from collegedata
        emoji_name = collegedata[index][2]

        # Upload emoji with the corresponding name from collegedata
        upload_emoji(image_file, emoji_name)

finally:
    # Close the driver after operations
    driver.quit()