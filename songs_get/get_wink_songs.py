from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def perform_scroll_and_click(driver, scroll_height):
    # Scroll down to a specific height
    driver.execute_script(f"window.scrollTo(0, {scroll_height});")
    WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-secondary.dark\:bg-wynk-dark-background.dark\:hover\:bg-black-secondary.dark\:text-wynk-dark-subtitle-gray.dark\:hover\:text-wynk-dark-gray-hover.pr-2.pl-3.text-sm.font-medium'))
    )
    driver.implicitly_wait(10)
    # Wait for a short moment for the content to load (you may adjust the sleep duration)

def fetch_playlist_songs(driver):
    # Wait for the presence of the elements with the specified class
    WebDriverWait(driver, 10).until(
        
        EC.presence_of_element_located((By.CSS_SELECTOR, '.jsx-7c093e1a359b5feb.text-title.font-normal.line-clamp-1.md\\:line-clamp-2.text-sm.hover\\:underline'))
    )

    # Get the page source after the final scroll and click
    page_source = driver.page_source

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all elements with the specified class
    song_elements = soup.find_all('a', class_='jsx-7c093e1a359b5feb text-title font-normal line-clamp-1 md\\:line-clamp-2 text-sm hover\\:underline')


    # Extract the song names
    song_names = [song.text.strip() for song in song_elements]

    return song_names

def main():
    # Set up the Selenium WebDriver (make sure you have the correct WebDriver installed, e.g., chromedriver for Chrome)
    driver = webdriver.Chrome()

    try:
        # Open the provided URL
        url = "https://wynk.in/music/playlist/top-garhwali-songs/bb_1547461496317"
        driver.get(url)

        "jsx-7c093e1a359b5feb tabularItem flex items-center justify-between pl-1 md:pl-4 py-2 md:pr-3 rounded-lg border-transparent border w-full cursor-pointer dark:hover:shadow-dark hover:border-wynk-dark-border hover:cursor-default"
        "btn-secondary dark:bg-wynk-dark-background dark:hover:bg-black-secondary dark:text-wynk-dark-subtitle-gray dark:hover:text-wynk-dark-gray-hover pr-2 pl-3 text-sm font-medium"
        # Perform the first scroll and click
        perform_scroll_and_click(driver, 2000)
        first_button = driver.find_element(By.CSS_SELECTOR, "btn-secondary dark:bg-wynk-dark-background dark:hover:bg-black-secondary dark:text-wynk-dark-subtitle-gray dark:hover:text-wynk-dark-gray-hover pr-2 pl-3 text-sm font-medium")
        first_button.click()
        driver.implicitly_wait(10)


        # # Wait for the page to load after the first click
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-secondary.dark\\:bg-wynk-dark-background.dark\\:hover\\:bg-black-secondary.dark\\:text-wynk-dark-subtitle-gray.dark\\:hover\\:text-wynk-dark-gray-hover.pr-2.pl-3.text-sm.font-medium'))
        # )

        # Perform the second scroll and click
        perform_scroll_and_click(driver, 3000)
        second_button = driver.find_element(By.CSS_SELECTOR, "btn-secondary dark:bg-wynk-dark-background dark:hover:bg-black-secondary dark:text-wynk-dark-subtitle-gray dark:hover:text-wynk-dark-gray-hover pr-2 pl-3 text-sm font-medium")
        second_button.click()

        # Wait for the page to load after the second click
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-secondary.dark\\:bg-wynk-dark-background.dark\\:hover\\:bg-black-secondary.dark\\:text-wynk-dark-subtitle-gray.dark\\:hover\\:text-wynk-dark-gray-hover.pr-2.pl-3.text-sm.font-medium'))
        # )

        # # Perform the third scroll and click
        # perform_scroll_and_click(driver, 1500)
        # third_button = driver.find_element(By.CSS_SELECTOR, '.btn-secondary.dark\\:bg-wynk-dark-background.dark\\:hover\\:bg-black-secondary.dark\\:text-wynk-dark-subtitle-gray.dark\\:hover\\:text-wynk-dark-gray-hover.pr-2.pl-3.text-sm.font-medium')
        # third_button.click()

        # # Wait for the page to load after the third click
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.jsx-7c093e1a359b5feb.text-title.font-normal.line-clamp-1.md\\:line-clamp-2.text-sm.hover\\:underline'))
        )

        # Fetch all elements with the specified class after the final scroll and click
        result = fetch_playlist_songs(driver)

        # Print the result
        print("Songs in the playlist:")
        for index, song_name in enumerate(result, start=1):
            print(f"{index}. {song_name}")
    
    except Exception as e:
        print("Error")
        print(e)
    
    finally:
        print("Done")
        # Close the browser window when done
        driver.quit()

if __name__ == "__main__":
    main()
