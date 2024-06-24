from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

phoneNumber = 'telefon num'
textMessage = 'gönderilecek mesaj'

try:
# Burada qr kod beklenir 
    qrCodeWait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]/div[1]/div/div/div[2]/div/canvas'))
        )
finally:
    driver.implicitly_wait(10)

try:
# Burada sayfanın yüklenmesini kontrol etmek için pp beklenir 
    startWait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div/span/div/div[2]/div[2]/div/div/div/div/img'))
        )
finally:
    driver.implicitly_wait(10)

try:
# Burada yeni mesaj oluştur butonu beklenir 
    newMessageWait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/header/header/div/span/div/span/div[1]/div/span'))
        )
finally:
    driver.implicitly_wait(10)

# Burada yeni mesaj oluştur butonuna tıklanır 
newMessagePath = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/header/header/div/span/div/span/div[1]/div/span')
newMessagePath.click()


# Burada numara yazma alanı beklenir
try:
    searchNumWait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]/p'))
        )
finally:
    driver.implicitly_wait(10)

# Burada numara yazma alanına telefon numarası gönderilir
searchNumPath = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]/p')
searchNumPath.send_keys(phoneNumber)

try:
# Burada numarası yazılan kişinin profil fotoğrafı beklenir
    personWait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/img'))
        )
finally:
    driver.implicitly_wait(10)

# Burada numarası yazılan kişinin profil fotoğrafına tıklanır
personPath = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/img')
personPath.click()


try:
# Burada fotoğrafına tıklanılan kişi ile olan yazışmadaki yazı kutusuna beklenir
    messageBoxWait = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
        )
finally:
    driver.implicitly_wait(10)

# Burada fotoğrafına tıklanılan kişi ile olan yazışmadaki yazı kutusuna tıklanır
messageBoxPath = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
messageBoxPath.send_keys(textMessage)


# Burada fotoğrafına tıklanılan kişi ile olan yazışmadaki gönder butonuna basılır.
sendBtnPath = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
sendBtnPath.click()










input()