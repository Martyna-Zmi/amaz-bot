from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import csv


def normal_open():
    options = Options()
    options.add_experimental_option("detach", True)
    web_driver = webdriver.Chrome(options=options)
    return web_driver


def wait_for_element(attribute: str, value: str):
    if attribute == 'id':
        try:
            element_present = expected_conditions.presence_of_element_located((By.ID, value))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
            exit(-1)
    elif attribute == 'name':
        try:
            element_present = expected_conditions.presence_of_element_located((By.NAME, value))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
            exit(-1)
    else:
        print("Error")
        exit(-1)


def csv_to_list(filename: str):
    try:
        file = open(filename)
    except FileNotFoundError:
        print("Błąd: nieprawidłowa scieżka do pliku csv z danymi")
        exit(-1)
    data = []
    for row in csv.reader(file):
        data.append(row[0])


url = input("Podaj link do strony edycji informacji o aukcji: ")
driver = normal_open()
driver.get(url)
