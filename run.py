# version 1.0.0.202401131141

from datetime import datetime
import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




# browser settings
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# file paths
root = "D:/Work/Projects/python/btk/v1"
filePath = root + "/btk_data.json"

# create if not exist
print(str(datetime.now()) + " json dosyası oluşturuluyor ...")
open(filePath, "a+").close()




# DÖNGÜ ####################################################
def run():
  while True:

    # Get Pages
    data = []
    
    for pageI in range(181):
      page = pageI + 1

      # get page 
      driver.get("https://www.btk.gov.tr/kurul-kararlari?page=" + str(page))
      print(str(datetime.now()) + " BTK Sayfa " + str(page) + " Açılıyor ...")
      # wait = WebDriverWait(driver, 100)

      # Get loyals
      for i in range(10):
        x = int(i + 1)
        print(str(datetime.now()) + " " + str(page) + ". Sayfadaki kanunlara ulaşıldı ...")

        

        # loyal name - Karar Adı
        path = "//*[@id=\"__next\"]/div/div[1]/div/div[2]/section[2]/div[1]/div[" + str(x) + "]/h4"
        comp = driver.find_elements(By.XPATH, path)[0]
        loyalNameText = comp.get_attribute("innerHTML")
        print(str(datetime.now()) + " loyal name :" + loyalNameText)

        # loyal Datetime And No - Karar tarihi ve no
        path = "//*[@id=\"__next\"]/div/div[1]/div/div[2]/section[2]/div[1]/div[" + str(x) + "]/div/div[1]/div[2]/div"
        comp = driver.find_elements(By.XPATH, path)[0]
        loyalNameDatetimeAndNo = comp.get_attribute("innerHTML")
        print(str(datetime.now()) + " loyal datetime and no :" + loyalNameDatetimeAndNo)

        # loyal Unit Name - İlgili Birim
        path = "//*[@id=\"__next\"]/div/div[1]/div/div[2]/section[2]/div[1]/div[" + str(x) + "]/div/div[2]/div[2]/div"
        comp = driver.find_elements(By.XPATH, path)[0]
        loyalNameUnitName = comp.get_attribute("innerHTML")
        print(str(datetime.now()) + " loyal unit name :" + loyalNameUnitName)

        # loyal Stream Date - Yayım Tarihi
        path = "//*[@id=\"__next\"]/div/div[1]/div/div[2]/section[2]/div[1]/div[" + str(x) + "]/div/div[3]/div[2]/div"
        comp = driver.find_elements(By.XPATH, path)[0]
        loyalNameStreamDate = comp.get_attribute("innerHTML")
        print(str(datetime.now()) + " loyal stream datetime :" + loyalNameStreamDate)

        # loyal File link - Dosya
        path = "//*[@id=\"__next\"]/div/div[1]/div/div[2]/section[2]/div[1]/div[" + str(x) + "]/div/div[4]/div[2]/div/a"
        comp = driver.find_elements(By.XPATH, path)[0]
        loyalNameFileLink = comp.get_attribute('href')
        print(str(datetime.now()) + " loyal file link :" + loyalNameFileLink)

        
        
        # create object from variables
        loyalItem = {}
        loyalItem["loyal_name"] = loyalNameText
        loyalItem["datetime_and_no"] = loyalNameDatetimeAndNo
        loyalItem["unit_name"] = loyalNameUnitName
        loyalItem["stream_date"] = loyalNameStreamDate
        loyalItem["file_link"] = loyalNameFileLink
        # loyalItem["page_no"] = page
        # loyalItem["page_loyal_index"] = x

        data.append(loyalItem)

        # write data to json file
        jsonText = json.dumps(data)
        with open(filePath, "w", encoding="utf-8") as file:
          file.writelines(jsonText)
        file.close()


        time.sleep(0.5)
      
      time.sleep(5)


# events
try:
  run()
    
except BaseException as e:
  print(str(datetime.now()) + ' Failed to do something: ' + str(e))