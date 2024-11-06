from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tests.uteis import acessar, get_data_test
import time
from Tests.login import logar


def buscar_modelo(driver, data):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, data["path"])))
        driver.find_element(By.XPATH, data["path"]).send_keys(data["value"])

        time.sleep(1)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, data["expected_path"])))
        element_text = driver.find_element(By.XPATH, data["expected_path"]).text

        assert element_text == data["expected_value"], f"Teste falhou! Esperado:" + data["expected_value"] + \
                                                       " mas obteve: " + element_text

        driver.find_element(By.XPATH, data["path"]).clear()
        return True

    except Exception as e:
        print(e)
        return False


def editar_modelo(driver, data):
    try:
        if not buscar_modelo(driver, data):
            raise Exception("Nao foi possivel localizar o modelo")

        points_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, data["points_button"])))
        points_button.click()

        editar_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, data["edit_button"])))
        editar_button.click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, data["label_nome_path"])))
        element_text = driver.find_element(By.XPATH, data["label_nome_path"]).text

        assert element_text == data["label_nome_value"], f"Teste falhou! Esperado:" + data["label_nome_value"] + \
                                                         " mas obteve: " + element_text

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, data["descricao_path"])))

        driver.find_element(By.XPATH, data["descricao_path"]).clear()
        driver.find_element(By.XPATH, data["descricao_path"]).send_keys(data["descricao_new_value"])

        final_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, data["final_button"])))
        final_button.click()

        time.sleep(2)

        driver.refresh()

        if not buscar_modelo(driver, data):
            raise Exception("Nao foi possivel localizar o modelo")

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, data["descricao_inicio_path"])))
        element_text = driver.find_element(By.XPATH, data["descricao_inicio_path"]).text

        assert element_text == data["descricao_new_value"], f"Teste falhou! Esperado:" + data["descricao_new_value"] + \
                                                            " mas obteve: " + element_text

        return True

    except Exception as e:
        print(e)
        return False


def duplicar_modelo(driver, data):
    try:
        if not buscar_modelo(driver, data):
            raise Exception("Nao foi possivel localizar o modelo")

        points_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, data["points_button"])))
        points_button.click()

        duplicate_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, data["duplicate_button"])))
        duplicate_button.click()

        time.sleep(2)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, data["title"])))
        title = driver.find_element(By.XPATH, data["title"]).text

        title = title.split("•")

        data["value"] = title[1] + " (Cópia)"

        driver.refresh()

        if not buscar_modelo(driver, data):
            raise Exception("Nao foi possivel localizar o modelo")

        time.sleep(1)

        points_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, data["points_button"])))
        points_button.click()

        excluir_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, data["excluir_button"])))
        excluir_button.click()

        time.sleep(2)

        return True
    except Exception as e:
        print(e)
        return False


def executar_acao(driver, acao):
    try:
        if acao["tipo"] == "pesquisar":
            return buscar_modelo(driver, acao)

        if acao["tipo"] == "editar":
            return editar_modelo(driver, acao)

        if acao["tipo"] == "duplicar":
            return duplicar_modelo(driver, acao)
        

        return False

    except Exception as e:
        print(f"Erro ao executar a ação: {e}")
        return False


def activity_tests(url, tests):
    failed = []
    success = []

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    if not acessar(driver, url):
        raise Exception("Não foi possível acessar o site informado")

    login_data = get_data_test("Massas", "login.json")

    if logar(driver, login_data):
        for test in tests:
            result = executar_acao(driver, test)

            if result:
                success.append(test["description"])
            else:
                failed.append(test["description"])

            time.sleep(5)
            driver.refresh()

        driver.quit()

    return success, failed
