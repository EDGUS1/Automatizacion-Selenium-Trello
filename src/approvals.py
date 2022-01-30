import os
from dotenv import load_dotenv, find_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

from PIL import Image
from io import BytesIO
from datetime import datetime

from login import login

time = 35
now = datetime.timestamp(datetime.now())

try:
    load_dotenv(find_dotenv())

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


    driver.get(os.getenv('PAGE_URL'))

    login(driver, time,os.getenv('USER_EMAIL'),os.getenv('USER_PASSWORD'))

    # Ingresar al tablero
    WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/ul/li[1]/a'))).click()

    # Añadir tarjeta
    WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="board"]/div[1]/div/div[3]/a'))).click()
    WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="board"]/div[1]/div/div[2]/div/div[1]/div/textarea')))
    nuevo_tarjeta = driver.find_element(By.XPATH,'//*[@id="board"]/div[1]/div/div[2]/div/div[1]/div/textarea').send_keys(f'Nueva tarjeta {now}')

    WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="board"]/div[1]/div/div[2]/div/div[2]/div[1]/input'))).click()

    # Ingresar a tarjeta creada
    WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="board"]/div[1]/div/div[2]/a[last()]'))).click()

    # Ingresar a Aprobacion
    WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[3]/div/div[1]/span[1]/span'))).click()

    # Esperar que se abra el modal
    WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH,'//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/iframe')))
    WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/iframe')))

    # Cambiar de iframe
    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="chrome-container"]/div[4]/div/div[2]/div/div/div/iframe'))
    WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="approvalsForTrelloRoot"]/div/div/div[2]')))
    WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div/div/div/div[2]')))
    elem = WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH,'//*[@id="approvalsForTrelloRoot"]/div/div/div[2]')))
    elem.click()

    WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="approvalsForTrelloRoot"]/div/div/div/div[3]/div/div/div/button'))).click()

    WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="approvalsForTrelloRoot"]/div/div/div/div[4]/button'))).click()

    driver.switch_to.default_content()

    # Cerrar Aprobaciones
    WebDriverWait(driver, time).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="chrome-container"]/div[4]/div/div[1]/a'))).click()


    # Esperar a que se muestre las aprobaciones

    WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[5]/div/div/div[2]/iframe')))

    driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="chrome-container"]/div[3]/div/div/div/div[4]/div[5]/div/div/div[2]/iframe'))

    WebDriverWait(driver, time).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="approvalsForTrelloRoot"]/div/div/div/div[2]')))

    # Volver al contexto global
    driver.switch_to.default_content()

    driver.implicitly_wait(25)

    png = driver.get_screenshot_as_png()


    crop_image = Image.open(BytesIO(png))
    crop_image.save(f'images/approvals-{now}.png')

    print('----------------------------------------------------------------------------------------------')
    print(f'Finalizo sin errores - Approvals - {now}')
    print('----------------------------------------------------------------------------------------------')
    

except Exception as e:
    print('----------------------------------------------------------------------------------------------')
    print(f'Error Approvals: {str(e)}')
    print('----------------------------------------------------------------------------------------------')
finally:
    driver.quit()

