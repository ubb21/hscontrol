#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async
import datetime
import json

from unidecode import unidecode
from config import BOT_TOKEN

import subprocess as sp
import time as t

startTime = t.time();


def startme(bot, update):
    print("startme")
    update.message.reply_text('Hallo {}!'.format(update.message.from_user.first_name))

def myID(bot, update):
    update.message.reply_text('Deine ID ist:  {}.'.format(update.message.from_user.id))
    print("fertig")

def info(bot, update):
    print("info")
    endTime = t.time()
    time_taken =  endTime - startTime
    hours, rest = divmod(time_taken,3600)
    minutes, seconds = divmod(rest, 60)
    update.message.reply_text('Der Server ist seit: {} Stunden, {} Minuten {} Sekunden online.'.format(hours,minutes,seconds))

@run_async        
def mc(bot, update):
    print("MC")
    update.message.reply_text("Minecraft Server wurde gestartet.")
    sp.call("./StartOnce.sh",shell=True)
    
def main():
    u = Updater(token=BOT_TOKEN)
    d = u.dispatcher

    d.add_handler(CommandHandler('start', startme))
    d.add_handler(CommandHandler('info', info))
    d.add_handler(CommandHandler('myip', myID))
    d.add_handler(CommandHandler('mcstart', mc))
    u.start_polling(clean=True)
    u.idle()


if __name__ == '__main__':
    main()
