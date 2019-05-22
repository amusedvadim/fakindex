# this file starts every morning via Scheduled tasks on #pythonanywhere.com

import urllib.request, urllib.error, urllib.parse
import ssl
from models import URLs
import time
import requests
import passwords
from datetime import datetime

date = datetime.now()
date = date.strftime('%d.%m.%Y')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def send_to_bot(e):
    proxies = passwords.proxies
    token = passwords.token
    url = "https://api.telegram.org/bot"
    url += token
    method = url + "/sendMessage"
    chat_id = method + '?chat_id=' + passwords.chat_id
    link = chat_id + '&text=' + str(e)
    requests.post(link, proxies=proxies)


def check_urls():
    for url in URLs.query:
        try:
            response = urllib.request.urlopen(url.drug_url, context=ctx)
            #print(response, url)
        except urllib.error.HTTPError as e:
            e = 'Check URLs // ' + str(e) + ' ' + str(url)
            send_to_bot(e)
            #print(e)
        except urllib.error.URLError as e:
            e = 'Check URLs // ' + str(e) + ' ' + str(url)
            send_to_bot(e)
            #print(e)
        time.sleep(5)
    d = date + ' URLs are okay'
    #print(d)
    send_to_bot(d)


if __name__ == "__main__":
    check_urls()






