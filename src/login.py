from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login(driver,time_wait, username, password):
    
    # Dirigirse a la pagina de inicio de sesión
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/nav/div/a[1]'))).click()
    
    # Ingresar credenciales username
    WebDriverWait(driver, time_wait).until(EC.visibility_of_element_located((By.NAME,'user'))).send_keys(username)
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.ID,'login'))).click()

    # Esperar a los elementos
    WebDriverWait(driver, time_wait).until(EC.visibility_of_element_located((By.NAME,'password')))
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.ID,'login-submit')))
    WebDriverWait(driver, time_wait).until(EC.presence_of_element_located((By.NAME,'password')))
    
    # Ingresar credenciales password
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.NAME,'password'))).send_keys(password)
    
    # Iniciar sesión
    WebDriverWait(driver, time_wait).until(EC.element_to_be_clickable((By.ID,'login-submit'))).click()