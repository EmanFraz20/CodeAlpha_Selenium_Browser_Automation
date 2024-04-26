from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_experimental_option("detach", True)

#Set up Chrome driver service: download the web driver which is an automation tool that controls google chrome.
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service, options = options)

        
def scroll_slowly():
      x = 0
      while True:
          x += 1
          driver.execute_script('scrollBy(0, 50)') # Scroll down by pixels
          time.sleep(0.5)
          if x > 50:
              break


#navigate to a website
driver.get("https://www.thepalestineacademy.com/")
driver.maximize_window()
time.sleep(1)
      
        
def navigate_pages(driver, page_name):
      WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.XPATH, f"//a[contains(text(), '{page_name}')]")))
    
      # Find and click on the "Courses" link
      page = driver.find_element("xpath", f"//a[contains(text(), '{page_name}')]")
      page.click()
      # Wait for the page to load 
      driver.implicitly_wait(10)
      scroll_slowly()      
      
      
navigate_pages(driver, 'Courses')
navigate_pages(driver, 'Resources')
navigate_pages(driver,'Gaza Emergency')

time.sleep(5)
driver.quit()