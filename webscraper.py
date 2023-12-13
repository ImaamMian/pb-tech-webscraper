from selenium import webdriver
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
url = 'https://www.pbtech.co.nz/product/VGAGBV44093/Gigabyte-NVIDIA-GeForce-RTX-4090-AERO-OC-24GB-GDDR'
browser = webdriver.Chrome()
browser.get(url)

name = browser.find_element('xpath','//*[@id="main_container"]/div[3]/div/div[2]/div[1]/div/div[1]/h1')
price =  browser.find_element('xpath','//*[@id="main_container"]/div[3]/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/span[3]/span/span[2]') 


list = [name.text]
print(list)

file = open("GpuData.txt", "w")
file.write(list[0])
file.write(' Price: $'+price.text + ' Time: '+formatted_datetime)
file.close()


browser.quit()