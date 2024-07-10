import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Disclaimer
print("DISCLAIMER: This script may violate GitHub's community guidelines.")
print("Use this script for educational purposes only.")
print("To stop the script at any time, press Ctrl+C.")
print("--------------------------------------------------")

# Ensure the user reads and agrees to the disclaimer
agreement = input("Type 'agree' to continue: ").strip().lower()
if agreement != 'agree':
    print("You did not agree to the disclaimer. Exiting...")
    exit()

# Load environment variables from .env file
load_dotenv()

# Get GitHub credentials from environment variables
github_username = os.getenv("GITHUB_USERNAME")
github_password = os.getenv("GITHUB_PASSWORD")

# Prompt the user for the GitHub user repositories URL
default_repos_url = "https://github.com/ZigaoWang?tab=repositories"
repos_url = input(f"Enter the GitHub user repositories URL (default {default_repos_url}): ").strip()
repos_url = repos_url if repos_url else default_repos_url

# Function to log in to GitHub
def github_login(username, password):
    driver.get("https://github.com/login")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "login_field")
    password_input = driver.find_element(By.ID, "password")
    sign_in_button = driver.find_element(By.NAME, "commit")

    username_input.send_keys(username)
    password_input.send_keys(password)
    sign_in_button.click()
    time.sleep(2)

# Function to star repositories on the user's repositories page
def star_repositories(delay):
    driver.get(repos_url)
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

# Prompt the user for the speed mode
default_speed_mode = "random"

speed_mode_input = input(f"Enter speed mode (fast, medium, random) (default {default_speed_mode}): ").strip().lower()
speed_mode = speed_mode_input if speed_mode_input else default_speed_mode

# Set delay based on speed mode
if speed_mode == "fast":
    delay = 2  # 2 seconds
elif speed_mode == "medium":
    delay = 5  # 5 seconds
elif speed_mode == "random":
    delay = random.uniform(5, 10)  # Random delay between 5 and 10 seconds
else:
    print("Invalid speed mode. Defaulting to random.")
    delay = random.uniform(5, 10)  # Random delay between 5 and 10 seconds

print("Starting now")

# Create a new Chrome session
driver = webdriver.Chrome()

# Log in to GitHub
github_login(github_username, github_password)

# Star repositories
repos_starred = 0
try:
    repos_starred = star_repositories(delay)
except KeyboardInterrupt:
    print("Program interrupted by user.")

# Output the number of repositories starred
print(f"Total repositories starred: {repos_starred}")

# Close the browser
driver.quit()