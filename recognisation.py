import speech_recognition as sr
from os import path
import pydub
import time 
from pydub import AudioSegment
import urllib.request as urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://patrickhlauke.github.io/recaptcha")
wait = WebDriverWait(driver, 300)

print("Captcha detected")

driver.find_element(By.XPATH, "/html/body/div[1]")
driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[1]/div/div/iframe"))
driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]").click()

driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/iframe"))
time.sleep(20)
driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button").click()

link = driver.find_element(By.TAG_NAME, "a").get_attribute("href")
print (link)
 
url = link
file_name = "C:\\Users\\asus\\Documents\\eclipse-workspace\\PySelenium\\D11Login\\audio.mp3"
urllib.urlretrieve(url, file_name)
   
src = "C:\\Users\\asus\\Documents\\eclipse-workspace\\PySelenium\\D11Login\\audio.mp3"
dst = "C:\\Users\\asus\\Documents\\eclipse-workspace\\PySelenium\\D11Login\\audio.wav"
   
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
  
r = sr.Recognizer()
audio = 'C:\\Users\\asus\\Documents\\eclipse-workspace\\PySelenium\\D11Login\\audio.wav'
with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')
  
try:
    text = r.recognize_google(audio)
    print (text)
      
except Exception as e:
    print (e)