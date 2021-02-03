import asyncio
from bs4 import BeautifulSoup
import math
import os
import heroku3
import requests
url = os.environ.get("AMAZON_TRACK_URL", None)
price_needed = os.environ.get("BUDGET_AMAZON", None)
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
from fridaybot import bot
loggerchat = Config.PRIVATE_GROUP_BOT_API_ID
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)

if url:
  async def tracker():
      page = requests.get(url, headers = headers)
      soup = BeautifulSoup(page.content, 'html.parser')
      title = soup.find(id = "productTitle").get_text()
      price = soup.find(id = "priceblock_ourprice").get_text()
      title = title.strip()
      price = price[2:].split(',')
      price = float("".join(price))
      if(price <= price_needed):
          await bot.send_message(loggerchat, "The current price of " + title + " is Rs " + str(price)) 
          try:
            app = Heroku.app(Config.HEROKU_APP_NAME)
            heroku_var = app.config()
            del heroku_var['AMAZON_TRACK_URL']
            del heroku_var['BUDGET_AMAZON']
          except:
            pass
      else:
          logger.info("Test, Its working")
          
  def dummyfunc():
      bot.loop.create_task(tracker())
  bot.loop.call_later(10 * 60, dummyfunc)
