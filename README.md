# MinecraftDataTransferHelper
A handy helper for transferring minecraft online server data to offline server

Works on bungeecord with offline mode subserver

Normal offline mode server not yet tested

## How to use
put both `datatrans.py` and `statstrans.py` to your `server` file

execute both files, one for `.dat` and one for `.stats`

it will print out the stats of each file:

success: transfer success

file not found: can't find that file

already have file: make sure you run the data transfer before running your server

## How it works? What it does?
The .py file is actually a simple code that copy and renames user files with new corresponding offline uuid
