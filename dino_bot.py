import time
from typing import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver() -> webdriver.Chrome:
    """
    Initializes and returns a Chrome WebDriver instance.

    It uses webdriver-manager to automatically download and manage
    the appropriate ChromeDriver.

    Returns:
        webdriver.Chrome: The initialized Chrome WebDriver instance.
    """
    chrome_options = ChromeOptions()
    
    # Use webdriver-manager to handle ChromeDriver
    service = ChromeService(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("WebDriver initialized successfully.")
    return driver

def navigate_to_game(driver: webdriver.Chrome, url: str) -> None:
    """
    Navigates the WebDriver to the specified URL.

    Args:
        driver: The WebDriver instance.
        url: The URL to navigate to.
    """
    try:
        driver.get(url)
        print(f"Successfully navigated to: {url}")
    except TimeoutException:
        print(f"Timeout while trying to navigate to: {url}")
    except WebDriverException as e:
        print(f"WebDriver error: {e}")
    except Exception as e:
        print(f"General error navigating to {url}: {e}")
        raise

def main() -> None:
    """
    Main function to demonstrate basic browser control and navigation to the game.
    """
    driver: Optional[webdriver.Chrome] = None # Initialize driver as None
    game_url: str = "chrome://dino"

    try:
        driver = initialize_driver()
        navigate_to_game(driver, game_url)

        # Keep the browser open for a bit to see the game
        # In a real bot, this would be replaced by the game playing loop
        print("Game page opened. Browser will close in 10 seconds...")
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred in the main function: {e}")
    finally:
        if driver:
            print("Closing the WebDriver.")
            driver.quit() 

if __name__ == "__main__":
    main()