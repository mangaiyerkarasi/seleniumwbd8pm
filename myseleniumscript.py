from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open Google
    driver.get("https://www.google.com")
    
    # Wait for the page to load and verify the title
    WebDriverWait(driver, 10).until(
        EC.title_contains("Google")
    )
    
    print("✓ Successfully opened google.com")
    print(f"✓ Page title: {driver.title}")
    
    # Optional: Wait to see the result
    time.sleep(2)
    
except Exception as e:
    print(f"✗ Error: {e}")
    
finally:
    # Close the browser
    driver.quit()
    print("✓ Browser closed")
