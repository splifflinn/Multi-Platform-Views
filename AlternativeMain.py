# https://github.com/fxlur/Multi-Platform-Views

# https://github.com/fxlur

#█▀▀ ▀▄▀ █   █ █ █▀█   
#█▀  █ █ █▄▄ █▄█ █▀▄

import requests
import json

print('Made by github.fxlur ') 

usertxt = input("Link to Post: ")

url = (usertxt)

proxylist = []
with open('proxies.txt', 'r') as f:
	for line in f:
		line = line.replace('\n','')
		tmp = line.split(':')
		proxies = {

#'http': 'http://'+ tmp[0] + ':' + tmp[1] + '@' + tmp[2] + ':' + tmp[3] + '/', 
#'https': 'http://'+ tmp[0] + ':' + tmp[1] + '@' + tmp[2] + ':' + tmp[3] + '/', 

'http': 'http://' + '@' + tmp[0] + ':' + tmp[1] + '/', 
'https': 'http://' + '@' + tmp[0] + ':' + tmp[1] + '/', 
}

proxylist.append(proxies)

print(proxylist)
while True:
     try:
         for proxy in proxylist:
            session = requests.Session()
            r = session.get(url, proxies=proxy)
            break
     except:
            print("Skipped, Dead proxy")

print(r.json()['ip'])