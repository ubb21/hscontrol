#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import run_async

import datetime
import json

import socket
import mcrcon

from unidecode import unidecode
from config import BOT_TOKEN, ALLOW_USERS, HOST, PORT, PASSWORD

import subprocess as sp
import time as t

startTime = t.time();

def secure(id):
    if id in ALLOW_USERS:
        return True
    else:
        return False

def startme(bot, update):
    #print("startme")
    update.message.reply_text('Hallo {}!'.format(update.message.from_user.first_name))

def myID(bot, update):
    update.message.reply_text('Deine ID ist:  {}.'.format(update.message.from_user.id))
    #print("myip")

def ping(bot, update):
    update.message.reply_text('Ich streike!')
    #print("pong")

def info(bot, update):
    #print("info")
    if secure(update.message.from_user.id):
        calc(update)
    else:
        update.message.reply_text('Diese Anfrage ist nicht DSGVO konform, bitte wenden Sie sich an den Adminstrator.')

def calc(update):
    time_taken =  t.time() - startTime
    WE, rest = divmod(time_taken,3600)
    minutes, rests = divmod(rest, 60)
    seconds, milli = divmod(rests, 1)

    WE2, hours = divmod(WE, 24)
    WE3, days = divmod(WE2,7)
    WE4, week = divmod(WE3,12)
    years, monath = divmod(WE4,12)

    msg = 'Der Server ist seit:'
    if years > 0:
        msg += ' '
        if years == 1:
            msg += '{} Jahr'.format(int(years))
        else:
            msg += '{} Jahre'.format(int(years))
        
    if monath > 0:
        msg += ' '
        if monath == 1:
            msg += '{} Monat'.format(int(monath))
        else:
            msg += '{} Monate'.format(int(monath))
        
        
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

    msg +=' online.'
    update.message.reply_text(msg)

@run_async        
def mcstart(bot, update):
    #print("MC")
    if secure(update.message.from_user.id):
        update.message.reply_text("Der Minecraft-Server wurde gestartet.")
        sp.call("./StartOnce.sh",shell=True)
    else:
        update.message.reply_text("Bitte füllen Sie den Passierschein A38 aus.")

@run_async
def mcsave(bot, update):
    if secure(update.message.from_user.id):
        print("mcsave")
        send(bot, update, "save-all")
    else:
        update.message.reply_text("Bitte füllen Sie den Passierschein A38 aus.")

@run_async
def mcstop(bot, update):
    if secure(update.message.from_user.id):
        send(bot, update, "stop")
    else:
        update.message.reply_text("Bitte füllen Sie den Passierschein A38 aus.")

@run_async
def send(bot, update, commad):
    # Connect
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    try:
        # Log in
        result = mcrcon.login(sock, PASSWORD)
        if not result:
            print("Incorrect rcon password")
            return

        response = mcrcon.command(sock, commad)
        update.message.reply_text(response)
    except:
        update.message.reply_text("Error")
    finally:
        sock.close()
            
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
