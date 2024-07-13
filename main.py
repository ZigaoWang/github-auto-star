import os
import sys
# import time
import random
from urllib.parse import urlparse
from selenium import webdriver
# from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from engine import github_login, star_repositories, star_organization

if __name__ == '__main__':

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
        sys.exit(-1)

    # Load environment variables from .env file
    load_dotenv()

    # Get GitHub credentials from environment variables
    github_username = os.getenv("GITHUB_USERNAME")
    github_password = os.getenv("GITHUB_PASSWORD")

    o_input = True if input("User or Organization? [U/O]: ") == "O" else False

    default_speed_mode = "random"

    speed_mode_input = input(
        f"Enter speed mode (fast, medium, slow, random) (default {default_speed_mode}): ").strip().lower()
    speed_mode = speed_mode_input if speed_mode_input else default_speed_mode

    delay_dict = {"fast": 0.1, "medium": 1, "slow": 5, "random": random.uniform(0.1, 10)}
    # Set delay based on speed mode
    try:
        delay = delay_dict[speed_mode]
    except Exception as e:
        print("Wrong speed mode.")
        sys.exit(-1)

    # Star repositories
    repos_starred = 0
    page = 1

    if o_input:
        # Prompt the user for the GitHub user URL
        default_org_url = "https://github.com/OblivionOcean"
        org_url = input(f"Enter the GitHub Organization URL (default {default_org_url}): ").strip()
        org_url = org_url if org_url else default_org_url
        org_name = urlparse(org_url).path.strip("/")
        real_url = f"https://github.com/orgs/{org_name}/repositories"

        print("Starting now.")
        driver = webdriver.Chrome()
        github_login(github_username, github_password, driver)

        try:
            while True:
                starred_on_page = star_organization(page, delay, driver, real_url)
                if starred_on_page:
                    repos_starred += starred_on_page
                    page += 1
                else:
                    break
        except KeyboardInterrupt:
            print("Program interrupted by user.")

        # Output the number of repositories starred
        print(f"Total repositories starred: {repos_starred}")

    else:
        # Prompt the user for the GitHub user URL
        default_user_url = "https://github.com/ZigaoWang"
        user_url = input(f"Enter the GitHub user URL (default {default_user_url}): ").strip()
        user_url = user_url if user_url else default_user_url
        repos_url = f"{user_url}?tab=repositories"

        print("Starting now.")

        # Log in to GitHub
        driver = webdriver.Chrome()
        github_login(github_username, github_password, driver)

        try:
            while True:
                starred_on_page = star_repositories(page, delay, driver, repos_url)
                if starred_on_page:
                    repos_starred += starred_on_page
                    page += 1
                else:
                    break
        except KeyboardInterrupt:
            print("Program interrupted by user.")

        # Output the number of repositories starred
        print(f"Total repositories starred: {repos_starred}")

    # Close the browser
    driver.quit()
    sys.exit(0)
