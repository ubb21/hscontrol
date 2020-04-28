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

startTime = t.time();

# start the bot
def startme(bot, update):
    update.message.reply_text('Hallo {}!'.format(update.message.from_user.first_name))

# return id from user
def myID(bot, update):
    update.message.reply_text('Deine ID ist:  {}.'.format(update.message.from_user.id))

# Ping - Pong
def ping(bot, update):
    update.message.reply_text('Ich streike!')

# Information about service
def info(bot, update):
    if hs.secure(update.message.from_user.id):
        hs.calc(bot, update, startTime)
    else:
        update.message.reply_text('Diese Anfrage ist nicht DSGVO konform, bitte wenden Sie sich an den Adminstrator.')

@run_async        
def mcstart(bot, update):
    #print("MC")
    if hs.mcproc(update.message.from_user.id):
        print("start")
        update.message.reply_text("Der Minecraft-Server wurde gestartet.")
        sp.call("./StartOnce.sh",shell=True)
    else:
        update.message.reply_text("I don't think so.")

@run_async
def mcsave(bot, update):
    if hs.mcproc(update.message.from_user.id):
        print("save")
        hs.send(bot, update, "save-all")
        print("finish")
    else:
        update.message.reply_text("Bitte füllen Sie den Passierschein A38 aus.")

@run_async
def mcstop(bot, update):
    if hs.mcproc(update.message.from_user.id):
        print("stop")
        hs.send(bot, update, "stop")
        print("finish")
    else:
        update.message.reply_text("Bitte sehr, aber ohne mich.")

       
def main():
    u = Updater(token=BOT_TOKEN)
    d = u.dispatcher

    d.add_handler(CommandHandler('start', startme))
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
