from bot import InternetSpeedTwitterBot

CHROME_DRIVER_PATH = "/Users/parth_gpt/Development/chromedriver"

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()
