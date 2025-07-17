#!/usr/bin/env python

import telegram
import sys
import os
import datetime
import random
import logging, logging.handlers

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = 00000000 # Set here your chat ID group

absolute_path = os.path.dirname(os.path.abspath(__file__))
logger = None

def configureLogger() -> None:
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y/%m/%d %I:%M:%S')
    fh = logging.handlers.RotatingFileHandler(filename='heyGiulia.log', maxBytes=1000)
    fh.setFormatter(formatter)
    global logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(fh)

def getRandomMessage() -> str:
    random.seed()
    messages_path = os.path.join(absolute_path, "messages.txt")
    with open(messages_path, "r") as f:
        msg_list = f.read().splitlines()
        msg = random.choice(msg_list)
        return msg

def main() -> None:
    configureLogger()
    bot = telegram.Bot(token=TOKEN)
    try:
        msg = getRandomMessage()
        bot.sendMessage(chat_id=CHAT_ID, text=msg)
        logger.info(msg)
    except telegram.error.TelegramError as err:
        logger.error(err.message)

if __name__ == '__main__':
    main()
