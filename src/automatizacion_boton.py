import os
import time
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

now = datetime.timestamp(datetime.now())
time_wait = 35

try:
    load_dotenv(find_dotenv())

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.get(os.getenv('PAGE_URL'))

    login(driver, time_wait,os.getenv('USER_EMAIL'),os.getenv('USER_PASSWORD'))

    # Ingresar al tablero
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/ul/li[1]/a'))).click()

    # Crear nueva tarjeta
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="board"]/div[2]/div/div[3]/a'))).click()

    # Ingresar nombre de la tajerta
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="board"]/div[2]/div/div[2]/div/div[1]/div/textarea'))).send_keys(f'Nueva tarjeta {now}')

    # Guardar tarjeta
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="board"]/div[2]/div/div[2]/div/div[2]/div[1]/input'))).click()

    time.sleep(10)
    # Ingresar a la tarjeta
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="board"]/div[2]/div/div[2]/a[1]'))).click()

    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[4]/div/div/div[2]/div/a'))).click()
    
    # Unirse btn
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/section/div/div/a[4]'))).click()

    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/section/div/div/div[1]/div[2]/div/input'))).send_keys('Unirse')

    # Boton añadir
    time.sleep(10)
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/section/div/button'))).click()
    # WebDriverWait(driver, time_wait).until(EC.presence_of_element_located((By.XPATH,'//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[4]/div/div/div[2]/div[1]/a')))
    time.sleep(10)
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[4]/div/div/div[2]/div[1]/a'))).click()

    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="chrome-container"]/div[3]/div/div/a'))).click()

    time.sleep(10)

    png = driver.get_screenshot_as_png()

    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="board"]/div[2]/div/div[2]/a[1]'))).click()

    # Boton de editar
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="chrome-container"]/div[3]/div/div/div/div[5]/div[4]/div/div/div[1]/a'))).click()
    # Eliminar boton
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/section/div/div/div/a[2]'))).click()
    # confirmar
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/section/div/button'))).click()

    crop_image = Image.open(BytesIO(png))
    crop_image.save(f'images/boton-{now}.png')

    print('----------------------------------------------------------------------------------------------')
    print(f'Finalizo sin errores - Automatización boton - {now}')
    print('----------------------------------------------------------------------------------------------')
    

except Exception as e:
    print('----------------------------------------------------------------------------------------------')
    print(f'Error Automatización boton: {str(e)}')
    print('----------------------------------------------------------------------------------------------')
finally:
    driver.quit()
