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



#available_modal = browser.find_element(By.LINK_TEXT, "Check store stock levels").click()
#time.sleep(10)
try:
  l = [] #dont need to do list and sum u can just use sum only i added list to help me visualise while testing
  sum = 0
  available_modal = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.LINK_TEXT,'Check store stock levels'))).click()
  #available = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="js-desktop-stock-table-container"]/table/tbody/tr[19]/td[2]')))

  #doing for 19 because there are 19 main
  for i in range(1,20):
    available = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="js-desktop-stock-table-container"]/table/tbody/tr[{}]/td[2]'.format(i))))
    sum = sum +int(available.text)
    l.append(int(available.text))
  print(l)
  print(sum)
except:
  print('error')
  browser.quit()


file = open("GpuData.txt", "w")
file.write(list[0])
file.write(' Price: $'+ price.text + ' Time: '+ formatted_datetime +' Total number available at pb tech ' + str(sum))
file.close()

#test commit
browser.quit()
