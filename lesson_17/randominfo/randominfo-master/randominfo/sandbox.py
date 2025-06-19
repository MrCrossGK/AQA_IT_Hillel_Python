from os.path import abspath, join, dirname
import sys, glob, csv, pytz, shutil
from random import randint, choice, sample, randrange

full_path = lambda filename: abspath(join(dirname(__file__), filename))


def get_address():
    full_addr = []
    addrParam = ['street', 'landmark', 'area', 'city', 'state', 'country', 'pincode']
    for i in range(5, 10):
        addrFile = csv.reader(open(full_path('data.csv'), 'r'))
        allAddrs = []
        # print(list(addrFile))
        for addr in addrFile:
            # print(addr)
            try:
                if addr[i] != '':
                    allAddrs.append(addr[i])
            except:
                pass
        print(allAddrs)
        full_addr.append(choice(allAddrs))
    full_addr = dict(zip(addrParam, full_addr))
    return full_addr

get_address()
