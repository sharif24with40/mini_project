from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SIMILAR_ACCOUNT = "buzzfeedtasty"  

USERNAME = input("Enter your Instagram username: ")
PASSWORD = input("Enter your Instagram password: ")

class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        logging.info("WebDriver initialized.")

    def login(self):
        try:
            self.driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(4.2)

            decline_cookies_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]"
            cookie_warning = self.driver.find_elements(By.XPATH, decline_cookies_xpath)
            if cookie_warning:
                cookie_warning[0].click()
                logging.info("Cookie warning dismissed.")

          
            username = self.driver.find_element(by=By.NAME, value="username")
            password = self.driver.find_element(by=By.NAME, value="password")

            username.send_keys(USERNAME)
            password.send_keys(PASSWORD)

            time.sleep(2.1)
            password.send_keys(Keys.ENTER)

            time.sleep(4.3)

           
            save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
            if save_login_prompt:
                save_login_prompt.click()
                logging.info("Save login info dismissed.")

            time.sleep(3.7)

           
            notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
            if notifications_prompt:
                notifications_prompt.click()
                logging.info("Notifications prompt dismissed.")

            logging.info("Logged in successfully.")

        except (NoSuchElementException, TimeoutException) as e:
            logging.error(f"An error occurred during login: {e}")
            self.driver.quit()

    def find_followers(self):
        try:
            time.sleep(5)
            self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
            logging.info(f"Navigating to {SIMILAR_ACCOUNT}'s followers.")

            time.sleep(8.2)
            modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
            modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)

            for i in range(5):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(2)
                logging.info(f"Scrolled modal {i+1}/5 times.")

        except NoSuchElementException as e:
            logging.error(f"An error occurred while finding followers: {e}")
            self.driver.quit()

    def follow(self):
        try:
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
            follow_count = 0

            for button in all_buttons:
                try:
                    button.click()
                    follow_count += 1
                    logging.info(f"Followed {follow_count} users so far.")
                    time.sleep(1.1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                    cancel_button.click()
                    logging.warning("Follow attempt intercepted; canceled unfollow dialog.")

            logging.info(f"Finished following users. Total followed: {follow_count}")

        except NoSuchElementException as e:
            logging.error(f"An error occurred during following: {e}")
            self.driver.quit()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
