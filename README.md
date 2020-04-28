# README
This is a telegram bot to control for a server.
It allows you to run predefined options - without connecting to SSH.

## General commands:
* info - duration of the bot / server
* start - The user starts the chat connection with this command (and the server answers)
* myid - returns the ID of the sender
* ping - server answers
* about - about the bot

## Special Minecraft CMDS
* mcstart - Starts the Minecraft server, which is located in the same folder
* mcstop - stop the Minecraft Server (RCON)
* mcsave - saving the world (RCON)

## Installation
Start the file: **install.sh** on Linux

## Start the Telegram bot
### First start
First, you must create the config.py with the copy command **cp configEXAMPLE.py config.py**

Then open this newly created file with nano or something similar and insert the token, as well as the Telegram ID, if you want to secure the server.

### Create bot
Write the @BotFather on Telegram and create your bot.

### Start bot
The bot can be started using the file **start.sh**.

### Do you have Windows?
Then I would be happy if you would pass on your installation instructions.

## How to start the minecraft server
Download your desired Minecraft server version and copy it to the bot folder.
Start the server using a script that you specified in main.py.
I recommend starting it on a screen.
