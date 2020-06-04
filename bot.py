#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Telegram API
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async

# Python Lib
import datetime
import json
from unidecode import unidecode
import subprocess as sp
import time as t

# HS Lib
import hslib as hs

# Config data
from config import BOT_TOKEN

import language as lang

startTime = t.time();

# start the bot
@run_async
def startme(bot, update):
    update.message.reply_text(lang.HELLO.format(update.message.from_user.first_name))

# return id from user
@run_async
def myID(bot, update):
    update.message.reply_text(lang.YOURID.format(update.message.from_user.id))

# Ping - Pong
@run_async
def ping(bot, update):
    update.message.reply_text(lang.PING)

# Information about service
@run_async
def info(bot, update):
    if hs.secure(update.message.from_user.id):
        hs.calc(bot, update, startTime)
    else:
        update.message.reply_text(lang.ABOUT)

@run_async        
def mcstart(bot, update):
    #print("MC")
    if hs.mcproc(update.message.from_user.id):
        print("start")
        update.message.reply_text(lang.MCSTART)
        sp.call("./StartOnce.sh",shell=True)
    else:
        update.message.reply_text(lang.NOWORK)

@run_async
def mcsave(bot, update):
    if hs.mcproc(update.message.from_user.id):
        print("save")
        hs.send(bot, update, "save-all")
        print("finish")
    else:
        update.message.reply_text(lang.NOWORK)

@run_async
def mcstop(bot, update):
    if hs.mcproc(update.message.from_user.id):
        print("stop")
        hs.send(bot, update, "stop")
        print("finish")
    else:
        update.message.reply_text(lang.NOWORK)

@run_async
def about(bot, update):
    update.message.reply_text(lang.ABOUT)
       
# Main Methode
def main():
    u = Updater(token=BOT_TOKEN)
    d = u.dispatcher

    d.add_handler(CommandHandler('start', startme))
    d.add_handler(CommandHandler('about', about))
    d.add_handler(CommandHandler('ping', ping))
    d.add_handler(CommandHandler('info', info))
    d.add_handler(CommandHandler('myid', myID))
    
    d.add_handler(CommandHandler('mcstart', mcstart))
    d.add_handler(CommandHandler('mcsave', mcsave))
    d.add_handler(CommandHandler('mcstop', mcstop))
    
    u.start_polling(clean=True)
    u.idle()


if __name__ == '__main__':
    main()
