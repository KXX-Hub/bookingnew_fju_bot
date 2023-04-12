import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import utilities as utils

config = utils.read_config()
driver = webdriver.Chrome()
username = config.get("username")
password = config.get("password")
bookingnew_fju_url = "https://bookingnew.fju.edu.tw/index.php"


def driver_send_keys_xpath(locator, key):
    """Send keys to element.
    :param locator: Locator of element.
    :param key: Keys to send.
    """
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))).send_keys(key)


def driver_click_xpath(locator):
    """Click element.
    :param locator: Locator of element.
    """
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, locator))).click()


def login():
    driver.get(bookingnew_fju_url)
    driver.maximize_window()
    print(username , password)
    driver_click_xpath("/html/body/nav/div[1]/div/a")
    driver_send_keys_xpath("//*[@id='id']", username)
    driver_send_keys_xpath("//*[@id='pasw']", password)
    driver_click_xpath("/html/body/form/table/tbody/tr[4]/td[2]/input[1]")
    try:
        driver_click_xpath("/html/body/nav/div[1]/div/a")
    except TimeoutException:
        pass
    print("Login successfully.")
    time.sleep(10000)


if __name__ == '__main__':
    login()
