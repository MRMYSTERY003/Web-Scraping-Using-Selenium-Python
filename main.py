#importing modules 

from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os



#download the chrome driver and the enter the path of the chromedriver here if not sure then watch the tutorial link in readme file

driver = wb.Chrome(executable_path= 'chrome driver path')
driver.get('https://www.instagram.com')


#entering into instagram 

uname = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[name = 'username']")))
uname.send_keys('YOUR MAIL ID OR USERNAME')
pword = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[name = "password"]')))
pword.send_keys('PASSWORD')
login = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
login.click()
notnow = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
notnow.click()
notnow2 = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
notnow2.click()



#entering the hashtag into the search bar
hashtag = input('enter the username or hashtag: ')
search = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')))
search.send_keys(hashtag)
time.sleep(5) # Wait for 5 seconds
my_link = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/" + hashtag[1:] + "/')]")))
my_link.click()


#scrolling for 4 times
scroll = 4
for n in range(scroll):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)


#getting the instagram posts links
ancher = driver.find_elements_by_tag_name('a')
ancher = [a.get_attribute('href') for a in ancher]
ancher = [a for a in ancher if str(a).startswith('https://www.instagram.com/p/')]
#print(ancher)


#getting the actual link

images = []
for i in ancher[:10]:
    driver.get(i)
    time.sleep(5)
    img = driver.find_elements_by_tag_name('img')
    img = [j.get_attribute('src') for j in img]
    images.append(img[1])


#downloading the images using wget module 

import wget
try:
    path = os.getcwd()
    path = os.path.join(path, hashtag[1:]+'s')
    os.mkdir(path)
except:
    path = os.getcwd()+'\\'+hashtag[1:]+'s'

i = 0
for image in images[:10]:
    save_as = os.path.join(path, hashtag[1:]+str(i)+'.jpg')
    wget.download(image, save_as)
    i+=1
print('completed...')
