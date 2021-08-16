# MinecraftDataTransferHelper
A handy helper for transferring minecraft online server data to offline server

Works on bungeecord with offline mode subserver

Normal offline mode server not 100% working

## Prep file
uuid.json file:
```
{
    "Steve": "8667ba71-b85a-4004-af54-457a9734eed7",
    "Alex": "ec561538-f3fd-461d-aff5-086b22154bce"
}
```

## How to use
You have to prepare a uuid.json file(attached in main)

the uuid behind the names have to be the real uuid from mojang

why i don't get the uuid directly from api.mojang?
cuz im lazy¯\_(ツ)_/¯
~~maybe do it in the future~~

put both `uuid.json` and `datatrans.py/statstrans.py` in the same directroy

for data:
put your original playerdata file from your world save in the same directory as those mentioned above and rename it as `data`
for stats:
put your original stats file from your world save in the same directory as those mentioned above and rename it as `s`

execute the `datatrans.py` or `statstrans` file

the program will list out the playerlist with online uuid and offline uuid
it also shows if it can find the file or not

after execution there should be a new file called `playerdata` or `stats` in the directory where the .py file is

in the `playerdata` or `stats` file are the renamed data with player's offline uuid
put those file back to your world save and that's all

## How it works? What it does?
The .py file is actually a simple code that copy and renames user files with new corresponding offline uuid
