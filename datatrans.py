import json
import shutil
import requests

# loc
src = r'.\world\playerdata\loc.dat'
dst = r'.\\world\playerdata\loc.dat'


# get offline uuid
def offline_uuid(name):
    url = f'http://tools.glowingmines.eu/convertor/nick/{name}'
    r = requests.get(url).json()
    print('offline: ', r['offlinesplitteduuid'])
    return r['offlinesplitteduuid']


# main
with open('usercache.json', 'r', encoding='utf-8') as f:
    js = json.load(f)
    for i in js:
        print(i['name'] + ':')
        print('server uuid:', i['uuid'])
        try:
            nsrc = src.replace('loc', i['uuid'])
            ndst = dst.replace('loc', offline_uuid(i['name']))
            shutil.copy(nsrc, ndst)
        except FileNotFoundError:
            print('file not found:\n')
        except shutil.SameFileError:
            print('already have file')
        else:
            print('success')
