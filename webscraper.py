from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
url = 'https://www.pbtech.co.nz/product/VGAGLX040910/GALAX-NVIDIA-GeForce-RTX-4090-ST-24GB-GDDR6X-Graph'
browser = webdriver.Chrome()
browser.get(url)

name = browser.find_element('xpath','//*[@id="main_container"]/div[3]/div/div[2]/div[1]/div/div[1]/h1')
price =  browser.find_element('xpath','//*[@id="main_container"]/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/span[3]/span/span[2]') 

list = [name.text]
print(list)



available_modal = browser.find_element(By.LINK_TEXT, "Check store stock levels").click()
time.sleep(10)
available = browser.find_element('xpath','//*[@id="js-desktop-stock-table-container"]/table/tbody/tr[19]/td[2]')
l = [available.text]
print(l)


file = open("GpuData.txt", "w")
file.write(list[0])
file.write(' Price: $'+ price.text + ' Time: '+ formatted_datetime)
file.close()

#test commit
browser.quit()
