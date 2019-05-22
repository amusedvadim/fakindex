# this file starts every morning via Scheduled tasks on #pythonanywhere.com

from models import Prices
import passwords
import requests
from datetime import datetime, timedelta

import MySQLdb
import MySQLdb.cursors
import pandas as pd

date_today = datetime.now()
ic = date_today.isocalendar()
weeknumber = ic[1]
daynumber = ic[2]
delta = timedelta(days=daynumber-1)
date_first = date_today - delta
date_first = date_first.strftime('%Y/%m/%d')
date_today = date_today.strftime('%Y/%m/%d')


def connect_to_database():
    options = {
    'host': '9278838.mysql.pythonanywhere-services.com',
    'user': '9278838',
    'password': 'Q12345678',
    'db': '9278838$fakdb',
    'charset': 'utf8mb4',
    'cursorclass': MySQLdb.cursors.DictCursor
    }
    db = MySQLdb.connect(**options)
    db.commit()
    #db.autocommit(True)
    #db.close()
    #print('connected')
    return db

def send_to_bot(e):
    proxies = passwords.proxies
    token = passwords.token
    url = "https://api.telegram.org/bot"
    url += token
    method = url + "/sendMessage"
    chat_id = method + '?chat_id=' + passwords.chat_id
    link = chat_id + '&text=' + str(e)
    requests.post(link, proxies=proxies)

def get_df():
    db = connect_to_database()
    query_today = "select count(price) from Prices where date='" + str(date_today) + "' and price!=0"
    query_all = "select count(price) from Prices"
    query_zeroes = "select Stores.store_name, Drugs.drug_name from Prices left join Drugs on Prices.drug_id=Drugs.id left join Stores on Prices.store_id=Stores.id where price=0 and date='"  + str(date_today) + "'"
    cursor = db.cursor()
    cursor.execute(query_today)
    df_today = pd.read_sql_query(query_today, con=db)
    result_today = df_today.iloc[0]['count(price)']
    cursor.execute(query_all)
    df_all = pd.read_sql_query(query_all, con=db)
    result_all = df_all.iloc[0]['count(price)']
    cursor.execute(query_zeroes)
    df_zeroes = pd.read_sql_query(query_zeroes, con=db)
    bot_today = date_today + ' select Prices from today = ' + str(result_today)
    bot_all = date_today + ' select ALL from Prices = ' + str(result_all)
    query_pivot = "select Stores.store_name, Drugs.drug_name, count(price) from Prices left join Drugs on Prices.drug_id=Drugs.id left join Stores on Prices.store_id=Stores.id where price=0 and date between '" + str(date_first) + "' and '" + str(date_today) + "'group by store_name, drug_name"
    df_pivot = pd.read_sql_query(query_pivot, con=db)
    text_start = "START - - > Date: " + str(date_today) + ", week: " + str(weeknumber)
    text_finish = "Date: " + str(date_today) + ", week: " + str(weeknumber) + " < - - FINISH"
    send_to_bot(text_start)
    send_to_bot(bot_today)
    send_to_bot(bot_all)
    send_to_bot(df_zeroes)
    send_to_bot(df_pivot)
    send_to_bot(text_finish)

    #print(df_zeroes)
    #db.close()
    #print (df.shape)
    #return df

if __name__ == '__main__':
    get_df()

