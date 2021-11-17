from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "/Users/parth_gpt/Development/chromedriver"
TWITTER_EMAIL
TWITTER_PASS 
PROMISED_DOWN = 70
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)

        go_button = self.driver.find_element_by_class_name("js-start-test")
        go_button.click()

        sleep(60)

        down_tag = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = down_tag.text

        up_tag = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up = up_tag.text

        print(f"Down: {self.down}")
        print(f"Up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        sleep(5)


        email = self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        sleep(2)

        username = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(USERNAME)
        username.send_keys(Keys.ENTER)
        sleep(2)

        password = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        sleep(2)

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_button.click()
        sleep(4)

        tweet_text = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet_text.send_keys(
            f"Hey @netplusofficial, why is my internet speed Down: {self.down}/ Up: {self.up} when I pay for Down: {PROMISED_DOWN}/ Up: {PROMISED_UP}.")
        sleep(1)

        post = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        post.click()

        self.driver.quit()
