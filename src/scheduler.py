from dotenv import load_dotenv
import os 
import sys
import telegram
import asyncio
import schedule
import time
import datetime
import pytz

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()

def job():
    token = os.environ.get('telegramToken')
    bot = telegram.Bot(token = token)
    public_chat_name = '@Open2023test'

    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
        
    asyncio.run(bot.sendMessage(chat_id=public_chat_name,text="Current time = " + str(now)))
    
schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)