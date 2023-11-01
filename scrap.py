from selenium import webdriver
from selenium.webdriver import Chrome
import time 
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import csv


file_csv = "type.csv"
flieds = ['Chapter','Transcript Link']


c_names=[]
ks=[]


driver = webdriver.Chrome()
driver.get("https://nptel.ac.in/courses/106105167")
driver.maximize_window()


# Sleep to allow the page to load
time.sleep(1)

# Scroll down to load more content if needed
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Find and click the "downloads" section
downloads = driver.find_element(By.XPATH, "//span[contains(text(),'downloads')]")
downloads.click()
time.sleep(1)

# Find and click the "Transcripts" section
transcripts = driver.find_element(By.XPATH, "//h3[contains(text(),'Transcripts')]")
transcripts.click()
time.sleep(2)

# Find all elements with class "d-data"
d_data_elements = driver.find_elements(By.XPATH, "//div[contains(@class,'d-data')]")

# Iterate through each "d-data" element
try :

    for d_data in d_data_elements:

        select_language = d_data.find_element(By.XPATH, "//span[contains(text(),'Select Language')]")
        select_language.click()
        time.sleep(0.5)
        op_force = d_data.find_element(By.XPATH,("//ul[contains(@class,'pseudo-options show')]")).find_element(By.XPATH,"li[contains(text(),'english-Verified')]")
        op_force.click()
        outer = driver.find_element(By.CSS_SELECTOR,"div.data")
        delta = outer.rect['y']
        ActionChains(driver).scroll_by_amount(0,int(delta)).perform()
        time.sleep(0.5)
except selenium.common.exceptions.NoSuchElementException :
        chapters = d_data.find_elements(By.XPATH,"//span[contains(@class,'c-name')]")
        for c in chapters :
            c_names.append(c.text)

        links = driver.find_elements(By.TAG_NAME, "a")
        filtered_links = [link.get_attribute("href") for link in links if link.get_attribute("href").startswith("https://drive.google.com/")]
        for k in filtered_links :
            ks.append(k)



asd = dict(zip(c_names,ks))
for i,j in asd.items() :
    print(i,j)

