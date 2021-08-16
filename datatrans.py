import json
import shutil
import requests

#loc
src = r'.\data\loc.dat'
dst = r'.\playerdata\loc.dat'

#get offline uuid
def offline_uuid(name):
    url = f'http://tools.glowingmines.eu/convertor/nick/{name}'
    r = requests.get(url).json()
    print('offline: ', r['offlinesplitteduuid'])
    return r['offlinesplitteduuid']

with open('uuid.json', 'r', encoding = 'utf-8') as f:
    t = json.load(f)
    print(type(t))
    for i in t:
        print(str(i) + ':')
        print('online: ', t[i])
        try:
            nsrc = src.replace('loc', t[i])
            ndst = dst.replace('loc', offline_uuid(i))
            shutil.copy(nsrc, ndst)
        except FileNotFoundError:
            print('file not found:\n')
        else:
            print('success')
