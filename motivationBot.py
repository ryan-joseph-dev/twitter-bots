#!/usr/bin/python3.8

import tweepy
import logging
from config import create_api
from datetime import date
import calendar

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def tweet_motivation(api, day):
    logger.info("Tweeting motivation")
    
    happy_day = f"Happy {day}!"
    hashtag = "\n #test"
    
    tweet_message = f"{happy_day}{hashtag}"
    logger.info(f"{tweet_message}")
    
    media_list = list()
    response = api.media_upload('thankyou.gif')
    media_list.append(response.media_id_string)
    
    logger.info("Sending tweet")
    api.update_status(status=tweet_message, media_ids=media_list)
    
def get_day():    
    todays_date = date.today()
    today_name = calendar.day_name[todays_date.weekday()]
    logger.info(f"Today is {today_name}")
    return today_name

def main():
    api = create_api()
    day = get_day()
    tweet_motivation(api, day)


if __name__ == "__main__":
    main()
    
    
    