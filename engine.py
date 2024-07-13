import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


def github_login(username, password, driver):
    driver.get("https://github.com/login")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "login_field")
    password_input = driver.find_element(By.ID, "password")
    sign_in_button = driver.find_element(By.NAME, "commit")

    username_input.send_keys(username)
    password_input.send_keys(password)
    sign_in_button.click()
    time.sleep(5)


def star_repositories(page, delay, driver, url):
    driver.get(f"{url}&page={page}")
    time.sleep(3)

    # Find all star buttons on the page
    star_buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Star this repository')]")

    if not star_buttons:
        return False  # No star buttons found, likely end of repositories

    for button in star_buttons:
        try:
            button.click()
            time.sleep(delay)
        except Exception as e:
            print(f"Error clicking star button: {e}")

    return len(star_buttons)


def star_organization(page, delay, driver, url):
    driver.get(f"{url}?page={page}")
    time.sleep(3)
    success = 0
    links = []
    elements = driver.find_elements(By.XPATH, '//a[@data-testid="listitem-title-link"]')
    for element in elements:
        url = element.get_attribute("href")
        links.append(url)
    print(links)

    if not links:
        return False

    for link in links:
        try:
            driver.get(link)
            star_button = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Star this repository')]")[0]
            star_button.click()
            time.sleep(delay)
            success += 1
        except Exception as e:
            print(f"Error clicking star button: {e}")

    return success
