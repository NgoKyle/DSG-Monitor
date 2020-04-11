import requests
import time
import json
import config
import discord
import multiprocessing

from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook


links = []
skus = []
names = []

#get SKUs, Products name from URL
with open('links.txt','r') as f:
    for line in f:
        try:
            link = line.strip()
            r = requests.get(link)
            bsObj = BeautifulSoup(r.text, 'html.parser')

            name = bsObj.find("h1", {'itemprop':'name'}).text
            sku = bsObj.find("ul", {"class":"product-numbers"}).findAll("li")[1].find("span").text

            names.append(name)
            links.append(link)
            skus.append(sku)
        except:
            continue

for i in range(len(links)):
    print(names[i], skus[i], "\n " + links[i])

def main():
    for i in range(len(links)):
        p1 = multiprocessing.Process(target=worker, args=(i,))
        p1.start()

def worker(i):
    while True:
        start_time = time.time()
        ats = checkOnlineInventory(names[i], skus[i], links[i])
        if(int(ats) > 0 and checkFrontEnd(links[i])):
            message = time.strftime('%a %H:%M:%S') + "\tItem: {}\navailable to ship: {}\n{}".format(names[i], ats, links[i])
            discord.sendDiscord(message, 'online', skus[i], 'version1')
        print(time.strftime('%a %H:%M:%S') + "\t" + names[i] + "--- %s seconds ---" % (time.time() - start_time))

def checkOnlineInventory(name, sku, link):
    try:
        r = requests.get('https://availability.dickssportinggoods.com/v1/inventoryapis/searchinventory?location=0&sku={}'.format(sku),
            headers=config.header, proxies=config.proxy).json()
    except:
        return checkOnlineInventory(name, sku, link)

    return r['data']['skus'][0]['atsqty']

def checkFrontEnd (link):
    try:
        r = requests.get(link, proxies=config.proxy, headers=config.header)
        bsObj = BeautifulSoup(r.text, 'html.parser')
        button = bsObj.find("span", {"class": "ship-mode-message"}).text.strip()
        if "Ship to Me" in button:
            return True
    except:
        return checkFrontEnd(link)
    return False

if __name__ == "__main__":
    main()
