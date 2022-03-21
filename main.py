# https://github.com/fxlur/Multi-Platform-Views

# https://github.com/fxlur

#█▀▀ ▀▄▀ █   █ █ █▀█   
#█▀  █ █ █▄▄ █▄█ █▀▄

import webbrowser, time

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


url = input("URL: ")
delay = input("Delay: ")

while True:
         webbrowser.open_new(url)
         time.sleep(int(delay))

def extract(proxy):
    proxy = random.choice(proxylist)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    try:
        r = requests.get(url, headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
        print(r.json(), ' | Works')
    except:
        pass
    return 