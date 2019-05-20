from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import numpy as np
from datetime import datetime, timedelta
import passwords
import json
import plotly
import plotly.graph_objs as go
import MySQLdb
import MySQLdb.cursors
import pandas as pd


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + passwords.user + ':' + passwords.password + '@' + passwords.host + '/' + passwords.db + '?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def connect_to_database():
    options = {
    'host': passwords.host,
    'user': passwords.user,
    'password': passwords.password,
    'db': passwords.db,
    'charset': 'utf8mb4',
    'cursorclass': MySQLdb.cursors.DictCursor
    }
    db = MySQLdb.connect(**options)
    db.commit()
    #db.autocommit(True)
    #db.close()
    #print('connected')
    return db

def get_df(query):
    db = connect_to_database()
    #query = 'select * from Prices'
    cursor = db.cursor()
    cursor.execute(query)
    df = pd.read_sql_query(query, con=db)
    db.close()
    return df


@app.route('/')
def fakindex():
    date_today = datetime.now()
    date_today_iso = date_today.isocalendar()
    delta = int(date_today_iso[2])
    last_sunday = date_today - timedelta(days=delta)
    ic = last_sunday.isocalendar()
    weeknumber = ic[1]
    last_monday = last_sunday - timedelta(days=6)
    first_day = datetime(2019, 4, 29)
    first_day_query = first_day.strftime('%Y/%m/%d')
    last_sunday_query = last_sunday.strftime('%Y/%m/%d')
    last_monday = last_monday.strftime('%d.%m.%Y')
    last_sunday = last_sunday.strftime('%d.%m.%Y')

    query = "select date, Stores.store_name, Drugs.drug_name, price from Prices left join Drugs on Prices.drug_id=Drugs.id left join Stores on Prices.store_id=Stores.id where date between '" + str(first_day_query) + "' and '" + str(last_sunday_query) + "'"
    df = get_df(query)

    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
    df['week'] = df['date'].dt.week
    df = df[['week', 'store_name', 'drug_name', 'price']]

    df['price'] = df['price'].replace(0, np.NaN)

    df = df.groupby(['week', 'store_name', 'drug_name']).mean()
    df = df.groupby(['week', 'store_name']).sum().reset_index()
    ###df['price'] = df['price'].map('{:,.0f}'.format)

    trace_wer = go.Scatter(
    x = df.loc[df['store_name'] == 'Wer.ru'].week,
    y = df.loc[df['store_name'] == 'Wer.ru'].price,
    mode = 'lines',
    name = 'wer.ru'
    )

    trace_366 = go.Scatter(
    x = df.loc[df['store_name'] == 'Аптека 36.6'].week,
    y = df.loc[df['store_name'] == 'Аптека 36.6'].price,
    mode = 'lines',
    name = 'Аптека 36.6'
    )

    trace_asna = go.Scatter(
    x = df.loc[df['store_name'] == 'Асна'].week,
    y = df.loc[df['store_name'] == 'Асна'].price,
    mode = 'lines',
    name = 'Асна'
    )

    trace_gorzdrav = go.Scatter(
    x = df.loc[df['store_name'] == 'Горздрав'].week,
    y = df.loc[df['store_name'] == 'Горздрав'].price,
    mode = 'lines',
    name = 'Горздрав'
    )

    trace_stoletov = go.Scatter(
    x = df.loc[df['store_name'] == 'Доктор Столетов'].week,
    y = df.loc[df['store_name'] == 'Доктор Столетов'].price,
    mode = 'lines',
    name = 'Доктор Столетов'
    )

    trace_neopharm = go.Scatter(
    x = df.loc[df['store_name'] == 'Неофарм'].week,
    y = df.loc[df['store_name'] == 'Неофарм'].price,
    mode = 'lines',
    name = 'Неофарм'
    )

    trace_rigla = go.Scatter(
    x = df.loc[df['store_name'] == 'Ригла'].week,
    y = df.loc[df['store_name'] == 'Ригла'].price,
    mode = 'lines',
    name = 'Ригла'
    )

    trace_samson = go.Scatter(
    x = df.loc[df['store_name'] == 'Самсон Фарма'].week,
    y = df.loc[df['store_name'] == 'Самсон Фарма'].price,
    mode = 'lines',
    name = 'Самсон Фарма'
    )

    trace_stolichki = go.Scatter(
    x = df.loc[df['store_name'] == 'Столички'].week,
    y = df.loc[df['store_name'] == 'Столички'].price,
    mode = 'lines',
    name = 'Столички'
    )

    trace_aptekaru = go.Scatter(
    x = df.loc[df['store_name'] == 'Apteka.ru'].week,
    y = df.loc[df['store_name'] == 'Apteka.ru'].price,
    mode = 'lines',
    name = 'Apteka.ru'
    )

    layout = go.Layout(
    xaxis={'title':'Номер недели'}, yaxis={'title':'Сумма, руб.'}
    )

    data_graph = [trace_wer, trace_366, trace_asna, trace_gorzdrav,
                        trace_stoletov, trace_neopharm, trace_rigla, trace_samson,
                        trace_stolichki, trace_aptekaru]

    graph = go.Figure(data=data_graph, layout=layout)
    graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)
    df = df.loc[lambda df: df['week'] == weeknumber]
    df = df.sort_values(by=['price'])
    df = df[['store_name', 'price']]

    store_0 = df.iloc[0]['store_name']
    store_1 = df.iloc[1]['store_name']
    store_2 = df.iloc[2]['store_name']
    store_3 = df.iloc[3]['store_name']
    store_4 = df.iloc[4]['store_name']
    store_5 = df.iloc[5]['store_name']
    store_6 = df.iloc[6]['store_name']
    store_7 = df.iloc[7]['store_name']
    store_8 = df.iloc[8]['store_name']
    store_9 = df.iloc[9]['store_name']

    price_0 = (df.iloc[0]['price'])
    price_1 = (df.iloc[1]['price'])
    price_2 = (df.iloc[2]['price'])
    price_3 = (df.iloc[3]['price'])
    price_4 = (df.iloc[4]['price'])
    price_5 = (df.iloc[5]['price'])
    price_6 = (df.iloc[6]['price'])
    price_7 = (df.iloc[7]['price'])
    price_8 = (df.iloc[8]['price'])
    price_9 = (df.iloc[9]['price'])

    percent_0 = '{:0,.2f}'.format(int(price_0) / int(price_9) * 100)
    percent_1 = '{:0,.2f}'.format(price_1 / price_9 * 100)
    percent_2 = '{:0,.2f}'.format(price_2 / price_9 * 100)
    percent_3 = '{:0,.2f}'.format(price_3 / price_9 * 100)
    percent_4 = '{:0,.2f}'.format(price_4 / price_9 * 100)
    percent_5 = '{:0,.2f}'.format(price_5 / price_9 * 100)
    percent_6 = '{:0,.2f}'.format(price_6 / price_9 * 100)
    percent_7 = '{:0,.2f}'.format(price_7 / price_9 * 100)
    percent_8 = '{:0,.2f}'.format(price_8 / price_9 * 100)
    percent_9 = '{:0,.2f}'.format(price_9 / price_9 * 100)

    price_0 = '{:0,.2f} руб.'.format(df.iloc[0]['price'])
    price_1 = '{:0,.2f} руб.'.format(df.iloc[1]['price'])
    price_2 = '{:0,.2f} руб.'.format(df.iloc[2]['price'])
    price_3 = '{:0,.2f} руб.'.format(df.iloc[3]['price'])
    price_4 = '{:0,.2f} руб.'.format(df.iloc[4]['price'])
    price_5 = '{:0,.2f} руб.'.format(df.iloc[5]['price'])
    price_6 = '{:0,.2f} руб.'.format(df.iloc[6]['price'])
    price_7 = '{:0,.2f} руб.'.format(df.iloc[7]['price'])
    price_8 = '{:0,.2f} руб.'.format(df.iloc[8]['price'])
    price_9 = '{:0,.2f} руб.'.format(df.iloc[9]['price'])

    return render_template("index.html", graphJSON=graphJSON, store_0=store_0, store_1=store_1, store_2=store_2,
                           store_3=store_3, store_4=store_4, store_5=store_5, store_6=store_6, store_7=store_7,
                           store_8=store_8, store_9=store_9, price_0=price_0, price_1=price_1, price_2=price_2,
                           price_3=price_3, price_4=price_4, price_5=price_5, price_6=price_6, price_7=price_7,
                           price_8=price_8, price_9=price_9, percent_0=percent_0, percent_1=percent_1,
                           percent_2=percent_2, percent_3=percent_3, percent_4=percent_4, percent_5=percent_5,
                           percent_6=percent_6, percent_7=percent_7, percent_8=percent_8, percent_9=percent_9)


if __name__ == '__main__':
    get_df()





