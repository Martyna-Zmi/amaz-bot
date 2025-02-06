from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import csv
import os


def normal_open():
    options = Options()
    options.add_experimental_option("detach", True)
    web_driver = webdriver.Chrome(options=options)
    return web_driver


def profile_open():
    chrome_profile_path = os.environ["CHROME_PROFILE_PATH"]
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('user-data-dir=' + chrome_profile_path)
    options.add_argument('--profile-directory=Profile 1')
    options.headless = False
    web_driver = webdriver.Chrome(options=options)
    return web_driver


def wait_for_element(attribute: str, attribute_name: str):
    if attribute == 'id':
        try:
            element_present = expected_conditions.presence_of_element_located((By.ID, attribute_name))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
            exit(-1)
    elif attribute == 'name':
        try:
            element_present = expected_conditions.presence_of_element_located((By.NAME, attribute_name))
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
        print("Error: invalid path to data file")
        exit(-1)
    data = []
    for row in csv.reader(file):
        data.append(row[0])
    data.pop(0)
    return data


data_list = csv_to_list("data.csv")
url = input("Please provide a link: ")
driver = profile_open()
driver.get(url)

for data_line in data_list:
    data_separated = data_line.split(";")
    # list indexes in data_separated:
    # 0 = attribute type
    # 1 = attribute name in html
    # 2 = value to fill
    wait_for_element(data_separated[0], data_separated[1])
    if data_separated[0] == "id":
        current_element = driver.find_element(by=By.ID, value=data_separated[1])
    elif data_separated[0] == "name":
        current_element = driver.find_element(by=By.NAME, value=data_separated[1])
    else:
        print("Invalid attribute type in data file")
        exit(-1)
    current_element.clear()
    current_element.send_keys(data_separated[2])
