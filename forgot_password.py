from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Tests.uteis import acessar

def forgot_password(driver, data):
    try:
        forgot_password_link = driver.find_elements(By.LINK_TEXT, "Esqueceu a senha?")

        if forgot_password_link:
            forgot_password_link = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Esqueceu a senha?")))

            forgot_password_link.click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))

        driver.find_element(By.XPATH, "//input[@type='email']").clear()
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(data["email"])

        reset_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Enviar')]")))
        reset_button.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, data["path"])))

        element_text = driver.find_element(By.XPATH, data["path"]).text

        time.sleep(2)

        assert element_text == data["expected_message"], f"Teste falhou! Esperado:" + \
                                                         data["expected_message"] + " mas obteve: " + element_text

        return True
    except Exception as e:
        print(e)
        return False

def forgot_password_tests(url, tests):
    failed = []
    success = []

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    acessar(driver, url)

    for test in tests:
        result = forgot_password(driver, test)

        if result:
            success.append(test["description"])
        else:
            failed.append(test["description"])

        time.sleep(2)
        
    driver.quit()

    return success, failed