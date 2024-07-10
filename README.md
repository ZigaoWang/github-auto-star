# GitHub Auto Star

## Description

GitHub Auto Star is a Python script that automates the process of starring repositories on a specified GitHub user's repository page. This script is intended for educational purposes only and may violate GitHub's community guidelines. Use it responsibly!

## Disclaimer

**DISCLAIMER:** This script may violate GitHub's community guidelines. Use this script for educational purposes only. The author is not responsible for any misuse of this script.

## Features

- Automatically log in to GitHub using your credentials.
- Star repositories on a specified user's repository page.
- Adjustable speed modes (fast, medium, slow, random).

## Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ZigaoWang/github-auto-star.git
    cd github-auto-star
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the appropriate ChromeDriver for your operating system and ensure it's in your system's PATH. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/).

4. Create a `.env` file in the root directory of the project and add your GitHub credentials:

    ```plaintext
    GITHUB_USERNAME=your_github_username
    GITHUB_PASSWORD=your_github_password
    ```

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Follow the on-screen instructions:

    - Agree to the disclaimer.
    - Enter the GitHub user URL (or press Enter to use the default).
    - Choose the speed mode (fast, medium, random).

3. The script will start starring repositories on the specified user's repository page.

## Example

```plaintext
--------------------------------------------------
  ______ __  __ __     __     ___       __         ______          
 / ___(_) /_/ // /_ __/ /    / _ |__ __/ /____    / __/ /____ _____
/ (_ / / __/ _  / // / _ \  / __ / // / __/ _ \  _\ \/ __/ _ `/ __/
/___/_/\__/_//_/\_,_/_.__/ /_/ |_\_,_/\__/\___/ /___/\__/\_,_/_/
--------------------------------------------------
GitHub Auto Star
Made by 💜 from Zigao Wang.
This project is licensed under MIT License.
GitHub Repo: https://github.com/ZigaoWang/github-auto-star/
--------------------------------------------------
DISCLAIMER: This script may violate GitHub's community guidelines.
Use this script for educational purposes only.
To stop the script at any time, press Ctrl+C.
--------------------------------------------------
Type 'agree' to continue: agree
Enter the GitHub user URL (default https://github.com/ZigaoWang): 
Enter speed mode (fast, medium, random) (default random): random
Starting now
Total repositories starred: 10
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Author

Made with 💜 by Zigao Wang.
