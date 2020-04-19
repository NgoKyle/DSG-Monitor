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
count = []

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

def main():
    for i in range(len(links)):
        count.append(0)
        p1 = multiprocessing.Process(target=worker, args=(i,))
        p1.start()

def worker(i):
    while True:
        start_time = time.time()
        ats = checkOnlineInventory(names[i], skus[i], links[i])
        if(int(ats) > 0):
            if checkFrontEnd(links[i]):
                message = time.strftime('%a %H:%M:%S') + "\n{}\nAvailable to ship: {}\n{}".format(names[i], ats, links[i])
                if int(count[i]) == 2:
                    discord.sendDiscord(message, 'online', skus[i], 'version2')
                elif int(count[i]) == 3:
                    discord.sendDiscord(message, 'online', skus[i], 'version3')
                elif int(count[i]) == 4:
                    discord.sendDiscord(message, 'online', skus[i], 'version4')
                count[i] = count[i] + 1
            else:
                count[i] = 0

        print(time.strftime('%a %H:%M:%S') + "\t" + names[i] + "\tcount:" + str(count[i]) + "\t--- %s seconds ---" % (time.time() - start_time))

def checkOnlineInventory(name, sku, link):
    try:
        tempHeaders = config.header
        tempHeaders['referer'] = link

        proxy = {
          "http": "http://108.59.14.203:13010",
          "https": "http://108.59.14.203:13010",
        }

        url = 'https://availability.dickssportinggoods.com/v1/inventoryapis/searchinventory?location=0&sku={}'.format(sku)
        r = requests.get(url, proxies=proxy, headers=tempHeaders ).json()
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
