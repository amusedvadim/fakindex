FAKindex Documentation
===

```text
- - - RUSSIAN BELOW  /  НА РУССКОМ НИЖЕ - - -
```

# About

FAKindex (First Aid Kit index) is a service that shows how much money you spend in a pharmacy to buy a first aid kit.

The first aid kit contains basic drugs which should be in every home.

Every day the service collects the prices of drugs and then calculates their average cost per week. The totals are summed up and the overall index is obtained.

The FAKindex is updated weekly on Mondays.

Location - Moscow, Russia

# Service functionality

- Daily price parsing from pharmacy websites.
- Daily report about the results of parsing to Telegram chat.
- Daily check of correct URLs.
- Calculation of the index and update data on the site.

Tech Stack: Python / SQLAlchemy / Flask / Plotly / Pandas / Beautifulsoup / MySQL / Bootstrap

# Structure

`app.py` - application for pythonanywhere.com

`app-local-machine.py` - application for local machine

`settings.py` - all the primary data for filling the database

`models.py` - create and fill database 

`parsers.py` - data parsers 

`check_parsers_to_bot.py` - report about the results of parsing to Telegram chat

`check_urls_to_bot.py` - check of correct URLs and report to Telegram chat


# Installing

I deployed this app in pythonanywhere.com, a web hosting service for programs based in Python. http://fakindex.ru

### Create your database

Go to https://www.pythonanywhere.com/user/YOUR_USERNAME/databases/, create new MySQL database and set your MySQL password.

### Create passwords.py

```python
# connection to database 
host = 'XXXX.mysql.pythonanywhere-services.com'  # your username in pythonanywhere.com
user = 'XXXX'  # your username in pythonanywhere.com
password = 'XXXX'  # your MySQL password
db = 'XXXX' #your database name

# connection to database via SSH from your local machine
ssh_username = 'XXXX' # your username in pythonanywhere.com
ssh_password = 'XXXX' # your password from pythonanywhere.com

#reporting to Telegram chat via bot
proxies = {'https':'socks5://NAME:PASSWORD@SERVER:PORT'} #proxy for Russians :)
token = 'XXXXX'    # token from @botfather
chat_id = 'XXXX'   # chat id to posting
```

### Run models.py

Run `models.py` for creating and filling database.

`settings.py` contains all the primary data for filling the database: pharmacy names, drug names and urls for parsers.

### Setup Scheduled tasks

Go to https://www.pythonanywhere.com/user/YOUR_USERNAME/tasks_tab/ and create 3 tasks

```text
For parsers
Daily at 01.00
Command: python3 /home/YOUR_PATH_TO_FILE/parsers.py
Expiry: never
```

```text
For checking results of parsing
Daily at 06.00
Command: python3 /home/YOUR_PATH_TO_FILE/check_parsers_to_bot.py
Expiry: never
```

```text
For checking urls 
Daily at 07.00
Command: python3 /home/YOUR_PATH_TO_FILE/check_urls_to_bot.py
Expiry: never
```

### Setup your web app

Go to https://www.pythonanywhere.com/user/YOUR_USERNAME/webapps and add a new web app.

# Support

I use Sequel Pro for connecting to database and make changes if something goes wrong. 
There can be 2 options.

1/ The url has changed and it needs to be changed in database.

2/ The drug wasn’t available in pharmacy and you need to add a price manually according to the rules for calculating the FAKindex:

- If the drug is not available on any of the days, this day is not considered
- If the drug wasn’t available for a week, its last parsed price is taken


# О проекте

FirstAidKit index | Индекс домашней аптечки - сервис, который показывает сколько денег вы потратите в той или иной аптеке, чтобы собрать домашнюю аптечку.

В домашнюю аптечку входят базовые лекарственные средства для оказания первой помощи и медикаментозного лечения, которые должны быть в каждом доме.

Каждый день сервис собирает цены на препараты, а затем рассчитывает их среднюю стоимость за календарную неделю. Итоговые показатели суммируются в единый пакет препаратов и получается общий индекс.

Индекс обновляется еженедельно по понедельникам.

Регион - город Москва.

# Функционал

- Ежедневный парсинг цен с сайтов аптек. 
- Ежедневный отчет в Телеграм чат о результатах парсинга. 
- Ежедневная проверка корректности ссылок. 
- Расчет индекса и обновление данных на сайте.

Tech Stack: Python / SQLAlchemy / Flask / Plotly / Pandas / Beautifulsoup / MySQL / Bootstrap

# Структура

`app.py` - приложение для pythonanywhere.com

`app-local-machine.py` - локальное приложение

`settings.py` - данные для заполнения БД 

`models.py` - создать и добавить данные в БД 

`parsers.py` - парсеры  

`check_parsers_to_bot.py` - отчет в Телеграм чат о результатах парсинга 

`check_urls_to_bot.py` - проверка корректности ссылок и отчет в Телеграм


# Установка

Я развернул приложение на pythonanywhere.com http://fakindex.ru/

### Создание базы данных

Перейдите https://www.pythonanywhere.com/user/YOUR_USERNAME/databases/, создайте новую MySQL БД и установите MySQL пароль.

### Создание passwords.py

```python
# соединение с БД 
host = 'XXXX.mysql.pythonanywhere-services.com'  # your username in pythonanywhere.com
user = 'XXXX'  # your username in pythonanywhere.com
password = 'XXXX'  # your MySQL password
db = 'XXXX' #your database name

# соединение с БД через SSH с локального компа
ssh_username = 'XXXX' # your username in pythonanywhere.com
ssh_password = 'XXXX' # your password from pythonanywhere.com

# настройка бота для отчетов в Телеграм
proxies = {'https':'socks5://NAME:PASSWORD@SERVER:PORT'} #proxy for Russians :)
token = 'XXXXX'    # token from @botfather
chat_id = 'XXXX'   # chat id to posting
```

### Запуск models.py

Запустите `models.py` для создания и наполнения базы данных.

`settings.py` содержит всю первичную информацию для заполнения базы данных - названия аптек, препаратов и ссылки для парсинга.

### Установка заданий по расписанию

Перейдите https://www.pythonanywhere.com/user/YOUR_USERNAME/tasks_tab/ и создайте 3 задания

```text
Для парсеров
Daily at 01.00
Command: python3 /home/YOUR_PATH_TO_FILE/parsers.py
Expiry: never
```

```text
Для проверки работы парсеров и отправки результатов в Телеграм
Daily at 06.00
Command: python3 /home/YOUR_PATH_TO_FILE/check_parsers_to_bot.py
Expiry: never
```

```text
Для проверки корректности URLs  и отправки результатов в Телеграм
Daily at 07.00
Command: python3 /home/YOUR_PATH_TO_FILE/check_urls_to_bot.py
Expiry: never
```

### Установка web app

Перейдите https://www.pythonanywhere.com/user/YOUR_USERNAME/webapps и добавьте новое web app.

# Поддержка

Я использую Sequel Pro для подключения к БД с локальной машины и внесения изменений в базу, если что-то пойдет не так. 
Может быть 2 варианта:

1/ Изменилась ссылка на препарат и ее нужно изменить в БД

2/ Препарата не было в наличии и нужно добавить его цену вручную согласно правилам расчета индекса:

- Если в какой-то из дней препарата нет в наличии, этот день не считается
- Если препарата не было в наличии неделю, берется его последняя зафиксированная цена


