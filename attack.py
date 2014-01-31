from netaddr import IPNetwork
import os
for ip in IPNetwork ('41.105.67.1/51'):
    os.system("python code.py "+str(ip))
