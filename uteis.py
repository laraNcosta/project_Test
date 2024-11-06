from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import json

def acessar(driver, url):
    driver.get(url)
    if driver.current_url == url:
        return True

    print(f"URL incorreta. Esperado: {url}, mas obteve: {driver.current_url}")
    return False


def get_data_test(folder, file):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, folder, file)

    with open(file_path, 'r', encoding='utf-8') as f:
        result = f.readlines()
        json_string = ''.join(result)
        json_object = json.loads(json_string)
        return json_object