from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fridaybot.modules.sql_helper.amazon_tracker_sql import add_new_tracker, is_tracker_in_db, rm_tracker, get_tracker_info, rm_tracker, get_all_tracker, get_all_urls
import requests
from bs4 import BeautifulSoup

@friday.on(friday_on_cmd(pattern="amt"))
async def _(event):
    hmm = event.text.split(" ", maxsplit=1)[1]
    try:
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id = "productTitle").get_text()
        price = soup.find(id = "priceblock_ourprice").get_text()
        title = title.strip()
        price = price[2:].split(',')
        price = float("".join(price))
    except:
        await event.edit("**Invalid Url !**")
        return
    if is_tracker_in_db(str(url)):
        await event.edit("**Tracker Already Found In Db**")
        return
    add_new_tracker(url, price)
    await event.edit(f"Product Name : {title} \nCurrent Price : {price} \n**Added To TrackerList**")
    
@friday.on(friday_on_cmd(pattern="rmt"))
async def _(event):
    hmm = event.text.split(" ", maxsplit=1)[1]
    if not is_tracker_in_db(str(url)):
        await event.edit("**Tracker Not Found In Db**")
        return
    rm_tracker(str(url))
    await event.edit(f"**Sucessfully Removed From TrackerList**")
    
ws = get_all_urls() 

if len(ws) != 0:
  async def track_amazon():
      kk, pp = get_all_tracker()
      for url.amazon_url in kk:
          for pm.budget in pp:
            page = requests.get(url, headers = headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(id = "productTitle").get_text()
            price = soup.find(id = "priceblock_ourprice").get_text()
            title = title.strip()
            price = price[2:].split(',')
            price = float("".join(price))
            if (price <= pm):
                await borg.send_message(Config.PRIVATE_GROUP_ID, f"#Tracker - Price Reduced \nProduct Name : {title} \nCurrent price : {price}")
                rm_tracker(str(url))
            else:
                pass

  scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
  scheduler.add_job(track_amazon, trigger="cron", hour=23, minute=59)
  scheduler.start()
