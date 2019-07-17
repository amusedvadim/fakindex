# this file starts every night via Scheduled tasks on #pythonanywhere.com

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from datetime import datetime
import time
import re
import random

from models import db_session, Drugs, Stores, URLs, Prices

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

date = datetime.now()
date = date.strftime('%Y/%m/%d')


# Parser https://samson-pharma.ru
def samsonpharma_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 1).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:
                prices_all = soup.findAll(attrs={"class": "product__price-value"})
                price = prices_all[0].text
                price = re.findall('(\d+)', price)
                price = price[0] + '.00'

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        time.sleep(15)

    db_session.commit()


# Parser http://www.neopharm.ru/
def neopharm_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 2).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:
                prices_all = soup.find(attrs={"class": "product__item__price"})
                price = prices_all.text
                price = re.findall('(\d+)', price)
                price = price[0] + '.00'

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        time.sleep(15)

    db_session.commit()


# Parser https://www.asna.ru/
def asna_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 3).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:
                prices_all = soup.find(attrs={"itemprop": "price"})
                price = prices_all.get('content')

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        time.sleep(15)

    db_session.commit()


# Parser https://366.ru/
def apteka366_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 5).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:
                prices_all = soup.find(attrs={"itemprop": "price"})
                price = prices_all.get('content')

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        time.sleep(15)

    db_session.commit()


# Parser https://apteka.ru/
def aptekaru_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 6).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:

                try:
                    prices_all = soup.find(attrs={"class": "price m--mobile_font "})
                    price = prices_all.span.text

                except:
                    prices_all = soup.find(attrs={"class": "price new_price m--mobile_font "})
                    price = prices_all.span.text

                else:
                    pass

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        #time.sleep(15)
        time.sleep(random.randint(21, 38))

    db_session.commit()


# Parser http://www.rigla.ru/
def rigla_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 7).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:
                prices_all = soup.find(attrs={"itemprop": "price"})
                price = prices_all.text
                price = price.replace(',', '.')

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        time.sleep(15)

    db_session.commit()


# Parser https://gorzdrav.org/
def gorzdrav_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 8).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:
                prices_all = soup.find(attrs={"itemprop": "price"})
                price = prices_all.get('content')

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        time.sleep(15)

    db_session.commit()


# Parser https://stoletov.ru/
def stoletov_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 9).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:
                price = soup.find(attrs={"class": "product-page__price-value"})
                price = price.text
                price = re.findall('(\d+)', price)
                price = price[0] + "." + price[1]

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        time.sleep(15)

    db_session.commit()


# Parser https://stolichki.ru/
def stolichki_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 10).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:
                prices_all = soup.findAll(attrs={"class": "productPrice__current"})
                price = prices_all[0].text
                price = re.sub(r'[^0-9.]+', r'', price)

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        time.sleep(15)

    db_session.commit()


# Parser https://wer.ru/
def wer_parser_to_db():

    for url in URLs.query.filter(URLs.store_id == 11).all():

        try:

            response = urllib.request.urlopen(url.drug_url, context=ctx).read()
            soup = BeautifulSoup(response, "html.parser")

            try:

                try:
                    price = soup.find(attrs={"class": " product-price price"})
                    price = price.text
                    price = re.findall('(\d+)', price)
                    price = price[0] + '.00'

                except:

                    try:
                        price = soup.find(attrs={"class": "product-newprice product-price"})
                        price = price.text
                        price = re.findall('(\d+)', price)
                        price = price[0] + '.00'

                    except:
                        price = soup.find(attrs={"class": "product-newprice product-price price"})
                        price = price.text
                        price = re.findall('(\d+)', price)
                        price = price[0] + '.00'

                    else:
                        pass

                else:
                    pass

            except:
                price = "0.00"

            if len(price) > 0:
                price = price
            else:
                price = "0.00"

        except TimeoutError:

            price = '0.00'

        except urllib.error.URLError:

            price = '0.00'

        except urllib.error.HTTPError:

            price = '0.00'

        drug = Drugs.query.filter(Drugs.id == url.drug_id).first()
        store = Stores.query.filter(Stores.id == url.store_id).first()

        to_db = Prices(date, drug, store, price)
        db_session.add(to_db)

        time.sleep(15)

    db_session.commit()

samsonpharma_parser_to_db()
time.sleep(25)
neopharm_parser_to_db()
time.sleep(25)
asna_parser_to_db()
time.sleep(25)
apteka366_parser_to_db()
time.sleep(25)
aptekaru_parser_to_db()
time.sleep(25)
rigla_parser_to_db()
time.sleep(25)
gorzdrav_parser_to_db()
time.sleep(25)
stoletov_parser_to_db()
time.sleep(25)
stolichki_parser_to_db()
time.sleep(25)
wer_parser_to_db()