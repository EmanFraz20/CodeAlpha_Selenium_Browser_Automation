from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By #search for elements in the HTML, once element accessed we can interact with it.
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time


options = Options()
options.add_experimental_option("detach", True)

 
#Set up Chrome driver service: download the web driver which is an automation tool that controls google chrome.
service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service = service, options = options)


#function to scroll the page     
def scroll_slowly(num):
      x = 0
      while True:
          x += 1
          driver.execute_script('scrollBy(0, 30)') # Scroll down by pixels
          time.sleep(0.5)
          if x > num:
              break
 
 

#navigate to a website
driver.get("https://www.thepalestineacademy.com/")
driver.maximize_window()
scroll_slowly(5)
driver.implicitly_wait(5)
#click on 'Start class' element
start_class = driver.find_element("xpath", "//div[contains(@class, 'fe-block fe-block-yui_3_17_2_1_1698638511092_12545')][//a[text()[contains(., 'Start class')]]]")
start_class.click()
      

        
def courses():
      scroll_slowly(3)
      
      # Wait for the link to exist
      WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'course-list__course-action course-list__header-content')]")))
      driver.implicitly_wait(10)
      #click on 'Start Course' element
      start_course = driver.find_element("xpath", "//div[contains(@class, 'course-list__course-action course-list__header-content')]")
      start_course.click()
      time.sleep(2)
      
      #expand the button
      click_button = driver.find_element("xpath", "//button[contains(@class, 'course-item__side-nav-toggle-button course-item__side-nav-toggle-button-desktop')]")
      click_button.click()
      time.sleep(2)
      
      #close the button
      close_button = driver.find_element("xpath", "//button[contains(@class, 'course-item__side-nav')]")
      close_button.click()
      
      
      
def gazaEmergency():
      
      # Wait for the link to exist
      WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Gaza Emergency')]")))
      # Find and click on the element named "Gaza Emergency" 
      last_page = driver.find_element("xpath", "//a[contains(text(), 'Gaza Emergency')]")
      last_page.click()
      
      scroll_slowly(42)
          
      # Click on the instagram ID of Motaz Azaiza
      WebDriverWait(driver, 5).until(
      EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'fe-block fe-block-yui_3_17_2_1_1698704516162_19084')]")))
      insta_id = driver.find_element("xpath", "//div[contains(@class, 'fe-block fe-block-yui_3_17_2_1_1698704516162_19084')]")
      insta_id = driver.find_element(By.XPATH, "//a[@href='https://www.instagram.com/motaz_azaiza/?hl=en']")
      insta_id.click()
      driver.switch_to.window(driver.window_handles[1])
      time.sleep(16)
      driver.switch_to.window(driver.window_handles[0])


      
#call the functions
courses()
gazaEmergency()
time.sleep(4)
driver.quit()