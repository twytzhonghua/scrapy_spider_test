import os, sys


with open('ret.txt', 'rb') as f:
    for line in f.readlines():
        out = line.decode('utf-8').split(' ')
        pre_name = out[0]
        last_name = pre_name + '_' + out[1].strip()
        file_name = pre_name + '.mp4'
        if os.path.exists(file_name):
            os.rename(file_name, last_name)










