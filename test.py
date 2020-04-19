import requests
import config
import json


s = requests.session()
#s.proxies.update(config.proxy)
s.headers.update(config.header)
s.get('https://www.dickssportinggoods.com/')
s.get("https://www.dickssportinggoods.com/p/powerblock-sport-50-lbadjustable-dumbbell-set-19pwkupwrblcksprtslc/19pwkupwrblcksprtslc?fbclid=IwAR2l7DCmJAVAb3yofHYkpqSjLOW2-SKt3GsG-lf3BePX44wyYc0aN5mu88o")

url = 'https://l.facebook.com/l.php?u=https%3A%2F%2Favailability.dickssportinggoods.com%2Fv1%2Finventoryapis%2Fsearchinventory%3Flocation%3D1401%26sku%3D16380346%26fbclid%3DIwAR0pF4O6Y4mdg6kfR8Rl9Gh_ZOvCyYW9bv_O91U4zjJTWe-I0U8453_CIbw&h=AT3WDtZF-gsbpshbowSNbKvKLDrk2lBLc9ciqyCGXOproIpaRgtv2VUIoVzmIzap4IUaTrYDJCXrM335PrxXcGsHglKLh9-Kn1vTWmY0NjADcD7tIsmz-6H0LBDd0MGteEAZGYIIVCU'

r = s.get(url)
print(r.text)
