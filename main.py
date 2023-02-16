from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib.request as request
from time import sleep

brave_path = "/usr/bin/brave-browser"
waitTime = 10
# userdatadir = "/home/cantor/.config/BraveSoftware/Brave-Browser/Default/"

op = webdriver.ChromeOptions()
op.binary_location = brave_path
# op.add_argument(f"--user-data-dir={userdatadir}")

driver = webdriver.Chrome(options=op)
driver.implicitly_wait(waitTime)



URL = "https://www.facebook.com/photo/?fbid=467126898842768&set=pcb.467127448842713"

driver.get(URL)

sleep(2)


print(driver.current_url)

urls = []
limit = 30
count = 0
while count < limit:
    # sleep(2)
    myPhoto = driver.find_element(By.CLASS_NAME, 'x4fas0m')
    imgurl = myPhoto.get_attribute('src')
    if imgurl in urls:
        break
    request.urlretrieve(imgurl, f"download_photos/photo{count}.jpg")
    print("Photo saved: ",count)
    urls.append(imgurl)


    while True:
        try:
            myDiv = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div')
            myDiv.click()
            break
        except:
            print("error while clicking")
            continue

    sleep(1)
    count += 1
    
for i,url in enumerate(urls):
    request.urlretrieve(url, f"download_photos/photo{i}.jpg")

print("Photos saved successfully")
a = input("Enter a key to exit")
sleep(2)





