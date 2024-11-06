from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.uteis import acessar
import time

def logar(driver, data):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))

        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(data["email"])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))

        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(data["password"])

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Entrar')]")))
        login_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["path"])))

        element_text = driver.find_element(By.XPATH, data["path"]).text

        time.sleep(2)

        assert element_text == data["expected_message"], f"Teste falhou! Esperado:" + data["expected_message"] +\
                                                         " mas obteve: " + element_text

        time.sleep(5)
        return True
    except Exception as e:
        print(e)
        return False

def login_tests(url, tests):
    failed = []
    success = []

    for test in tests:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        if not acessar(driver, url):
            raise Exception("Não foi possível acessar o site informado")

        result = logar(driver, test)

        if result:
            success.append(test["description"])
        else:
            failed.append(test["description"])

        driver.quit()

    return success, failed
