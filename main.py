#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async
import datetime
import json

from unidecode import unidecode
from config import BOT_TOKEN, ALLOW_USERS

import subprocess as sp
import time as t

startTime = t.time();

def secure(id):
    if id in ALLOW_USERS:
        return True
    else:
        return False

def startme(bot, update):
    print("startme")
    update.message.reply_text('Hallo {}!'.format(update.message.from_user.first_name))

def myID(bot, update):
    update.message.reply_text('Deine ID ist:  {}.'.format(update.message.from_user.id))
    print("myip")

def ping(bot, update):
    update.message.reply_text('Nein {}!'.format(update.message.from_user.first_name))
    print("pong")

def info(bot, update):
    print("info")
    if secure(update.message.from_user.id):
        endTime = t.time()
        time_taken =  endTime - startTime
        hours, rest = divmod(time_taken,3600)
        minutes, rests = divmod(rest, 60)
        seconds, milli = divmod(rests, 1)
        update.message.reply_text('Der Server ist seit: {} Stunden, {} Minuten {} Sekunden online.'.format(int(hours),int(minutes),int(seconds)))
    else:
        update.message.reply_text('Sie erhalten keine Informationen von mir.')

@run_async        
def mc(bot, update):
    print("MC")
    if secure(update.message.from_user.id):
        update.message.reply_text("Der Minecraft-Server wurde gestartet.")
        sp.call("./StartOnce.sh",shell=True)
    else:
        update.message.reply_text("Ich denke, sie duerfen es nicht!")
    
def main():
    u = Updater(token=BOT_TOKEN)
    d = u.dispatcher

    d.add_handler(CommandHandler('start', startme))
    d.add_handler(CommandHandler('ping', ping))
    d.add_handler(CommandHandler('info', info))
    d.add_handler(CommandHandler('myid', myID))
    d.add_handler(CommandHandler('mcstart', mc))
    u.start_polling(clean=True)
    u.idle()


if __name__ == '__main__':
    main()
