#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Telegram API
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async

# Python Lib
from unidecode import unidecode
import subprocess as sp
import time as t

# MC Lib
import socket
import mcrcon
## MC-RCON config
from config import MC_USERS, HOST, PORT, PASSWORD

from config import OP_USER

# Language
import language as lang

def mcproc(id):
    if id in MC_USERS:
        return True
    else:
        return False
    
def secure(id):
    if id in OP_USER:
        return True
    else:
        return False


def calc(bot, update, startTime):
    print("calc")
    time_taken =  t.time() - startTime
    WE, rest = divmod(time_taken,3600)
    minutes, rests = divmod(rest, 60)
    seconds, milli = divmod(rests, 1)

    WE2, hours = divmod(WE, 24)
    WE3, days = divmod(WE2,7)
    WE4, week = divmod(WE3,12)
    years, month = divmod(WE4,12)

    msg = lang.CALC1
    if years > 0:
        msg += ' '
        if years == 1:
            msg += '{} Jahr'.format(int(years))
        else:
            msg += '{} Jahre'.format(int(years))
        
    if month > 0:
        msg += ' '
        if month == 1:
            msg += '{} Monat'.format(int(month))
        else:
            msg += '{} Monate'.format(int(month))
        
        
    if week > 0:
        msg += ' '
        if week == 1:
            msg += '{} Woche'.format(int(week))
        else:
            msg += '{} Wochen'.format(int(week))

    if days > 0:
        msg += ' '
        if days == 1:
            msg += '{} Tag'.format(int(days))
        else:
            msg += '{} Tage'.format(int(days))
        
    if hours > 0:
        msg += ' '
        if hours == 1:
            msg += '{} Stunde'.format(int(hours))
        else:
            msg += '{} Stunden'.format(int(hours))
        
    if minutes > 0:
        msg += ' '
        if minutes == 1:
            msg += '{} Minute'.format(int(minutes))
        else:
            msg += '{} Minuten'.format(int(minutes))
        
    if seconds > 0:
        msg += ' '
        if seconds == 1:
            msg += '{} Sekunde'.format(int(seconds))
        else:
            msg += '{} Sekunden'.format(int(seconds))

    msg +=lang.CALC2
    update.message.reply_text(msg)


@run_async
def send(bot, update, commad):
    try:
        print("send")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        # Log in
        result = mcrcon.login(sock, PASSWORD)
        if not result:
            # Failed Log in
            update.message.reply_text(lang.WRONGPW)
            return
        response = mcrcon.command(sock, commad)
        update.message.reply_text(response)
        print(response)
    except:
        update.message.reply_text(lang.CONNECTIONLOST)
        print(lang.CONNECTIONLOST)
    finally:
        sock.close()
