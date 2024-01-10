from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
url = 'https://www.pbtech.co.nz/product/MEMGSK3828/GSKILL-Ripjaws-V-Series-16GB-DDR4-Desktop-RAM-Kit'
#url = 'https://www.pbtech.co.nz/product/VGAGLX040910/GALAX-NVIDIA-GeForce-RTX-4090-ST-24GB-GDDR6X-Graph' #this is for the 4090 gpu with units in stock
browser = webdriver.Chrome()
browser.get(url)

###note that the price is not same for all pages e.g. if no tax free shipping or no units available then the xpath is changed and will not work
name = browser.find_element('xpath','//*[@id="main_container"]/div[3]/div/div[2]/div[1]/div/div[1]/h1')
#price =  browser.find_element('xpath','//*[@id="main_container"]/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/span[3]/span/span[2]') 
price =  browser.find_element(By.CLASS_NAME,'js-dollar') 
price_cents = browser.find_element(By.CLASS_NAME,'js-cent') 
list = [name.text]
print(list)

#IMPORTANT: TRY TO CHANGE THE PRICE TO USE THE CLASS BECAUSE IT SEEMS ITS ONLY USED FOR THE PRICE AND NOTHING ELSE BECAUSE THE XPATH KEEPS CHANGING DEPENDING ON DIFF FACTORS SUCH AS HAVING NO UNITS AVAILABLE OR TAX FREE SHIPPING AVAILABLE

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
    if "+" in available.text:
      val = available.text.replace("+", "")
      print(val)
      sum = sum + int(val)
      l.append(int(val))
      print(sum)
    else:
      sum = sum + int(available.text)
      l.append(int(available.text))
  print(l)
  print(sum)
except Exception as e:
  print('error' ,str(e))
  browser.quit()


file = open("GpuData.txt", "w")
file.write(list[0])
file.write(' Price: $'+ price.text + price_cents.text + ' Time: '+ formatted_datetime +' Total number available at pb tech ' + str(sum))
file.close()

#test commit
browser.quit()
