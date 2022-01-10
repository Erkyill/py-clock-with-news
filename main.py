from datetime import datetime  # imports date and time
import time                    # importing sleep
from art import *              # ascii art to display cool clock
import feedparser              # checks rss for news
import os                      # to clean terminal

# Cleans terminal then time is set and printed with ascii characters.
# And then 3 newest news articles are posted under the clock
while True:
    os.system("clear")
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    tprint(current_time, "tarty1")

    crypto_news = feedparser.parse("https://cointelegraph.com/rss")

    for i in range(0, 3):
        blockchain_news = crypto_news.entries[i]
        print(f"[{blockchain_news.title}]")
    
    time.sleep(30)