from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_webdriver(headless = False,
                  download_directory = None):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,
        "download.default_directory": download_directory,
        "excludeSwitches": ["disable-automation"]
    })
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
