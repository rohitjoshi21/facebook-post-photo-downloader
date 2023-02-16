from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request as request
from time import sleep
import sys
import os


def get_url_from_args():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://www.facebook.com/photo?fbid=139334082361780&set=a.130296589932196"
    return url
        
    
waitTime = 10

#This code is written for brave-browser, but can be used for any browser with some minor edit on this part
browser_path = "/usr/bin/brave-browser"

op = webdriver.ChromeOptions()
op.binary_location = browser_path

driver = webdriver.Chrome(options=op)
driver.implicitly_wait(waitTime)


    
URL = get_url_from_args()
print("URL: ",URL)
driver.get(URL)

sleep(2)


directory = "downloaded_photos"
if not os.path.exists(directory):
    os.makedirs(directory)
    
urls = []

#Photo download limit, you can change this if you have more photos in the given post
limit = 30

count = 0
while count < limit:
    myPhoto = driver.find_element(By.CLASS_NAME, 'x4fas0m')
    imgurl = myPhoto.get_attribute('src')
    if imgurl in urls:
        break
    request.urlretrieve(imgurl, f"{directory}/photo{count}.jpg")
    print("Photo saved: ",count)
    urls.append(imgurl)

	#Searching for next button
    while True:
        try:
            myDiv = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div')
            myDiv.click()
            break
        except:
            print("error occured while clicking, retrying...")
            continue

    sleep(1)
    count += 1
    
print("Photos saved successfully")





