import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

# Logo and information
logo = r"""
  ______ __  __ __     __     ___       __         ______          
 / ___(_) /_/ // /_ __/ /    / _ |__ __/ /____    / __/ /____ _____
/ (_ / / __/ _  / // / _ \  / __ / // / __/ _ \  _\ \/ __/ _ `/ __/
/___/_/\__/_//_/\_,_/_.__/ /_/ |_\_,_/\__/\___/ /___/\__/\_,_/_/
"""
print("--------------------------------------------------")
print(logo)
print("GitHub Auto Star")
print("Made by 💜 from Zigao Wang.")
print("This project is licensed under MIT License.")
print("GitHub Repo: https://github.com/ZigaoWang/github-auto-star/")
print("--------------------------------------------------")

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

# Function to star repositories on a user's repositories page
def star_repositories(user_url, delay):
    page = 1
    repos_starred = 0
    while True:
        driver.get(f"{user_url}?tab=repositories&page={page}")
        time.sleep(3)

        # Find all star buttons on the page
        star_buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Star this repository')]")

        if not star_buttons:
            break  # No star buttons found, likely end of repositories

        for button in star_buttons:
            try:
                button.click()
                time.sleep(delay)
                repos_starred += 1
            except Exception as e:
                print(f"Error clicking star button: {e}")

        page += 1
    return repos_starred

# Function to star repositories of stargazers of a given repo
def star_stargazers(repo_url, delay):
    page = 1
    repos_starred = 0
    while True:
        driver.get(f"{repo_url}/stargazers?page={page}")
        time.sleep(3)

        # Find all stargazers
        stargazers = driver.find_elements(By.XPATH, "//a[@data-hovercard-type='user']")

        if not stargazers:
            break  # No stargazers found, likely end of stargazers

        for stargazer in stargazers:
            user_url = stargazer.get_attribute("href")
            repos_starred += star_repositories(user_url, delay)

        page += 1
    return repos_starred

# Function to star repositories of users you are following
def star_following(delay):
    page = 1
    repos_starred = 0
    while True:
        driver.get(f"https://github.com/{github_username}?tab=following&page={page}")
        time.sleep(3)

        # Find all following users
        following_users = driver.find_elements(By.XPATH, "//a[@data-hovercard-type='user']")

        if not following_users:
            break  # No following users found, likely end of following list

        for user in following_users:
            user_url = user.get_attribute("href")
            repos_starred += star_repositories(user_url, delay)

        page += 1
    return repos_starred

# Prompt the user for the mode
print("Select a mode:")
print("1. Single Person Mode")
print("2. Stargazers Mode")
print("3. Following Mode")
mode = input("Enter the mode number (1, 2, 3): ").strip()

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

# Execute the selected mode
repos_starred = 0
try:
    if mode == "1":
        # Single Person Mode
        default_user_url = "https://github.com/ZigaoWang"
        user_url = input(f"Enter the GitHub user URL (default {default_user_url}): ").strip()
        user_url = user_url if user_url else default_user_url
        repos_starred = star_repositories(user_url, delay)
    elif mode == "2":
        # Stargazers Mode
        default_repo_url = "https://github.com/torvalds/linux"
        repo_url = input(f"Enter the GitHub repository URL (default {default_repo_url}): ").strip()
        repo_url = repo_url if repo_url else default_repo_url
        repos_starred = star_stargazers(repo_url, delay)
    elif mode == "3":
        # Following Mode
        repos_starred = star_following(delay)
    else:
        print("Invalid mode selected. Exiting...")
except KeyboardInterrupt:
    print("Program interrupted by user.")

# Output the number of repositories starred
print(f"Total repositories starred: {repos_starred}")

# Close the browser
driver.quit()