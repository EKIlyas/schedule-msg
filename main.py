import schedule
import time
import os
import webbrowser


def recreation_msg():
    os.system('open recreation_msg')


def open_site(url):
    webbrowser.open(url)


schedule.every().day.at("08:00").do(open_site, 'https://www.google.ru/')
schedule.every().day.at("08:50").do(recreation_msg)
schedule.every().day.at("09:50").do(recreation_msg)
schedule.every().day.at("10:50").do(recreation_msg)
schedule.every().day.at("11:45").do(recreation_msg)

schedule.every().day.at("13:00").do(open_site, 'https://www.google.ru/')
schedule.every().day.at("13:25").do(recreation_msg)
schedule.every().day.at("13:55").do(recreation_msg)
schedule.every().day.at("14:25").do(recreation_msg)
schedule.every().day.at("14:55").do(recreation_msg)

schedule.every().day.at("15:15").do(open_site, 'https://www.google.ru/')
schedule.every().day.at("15:50").do(recreation_msg)
schedule.every().day.at("16:50").do(recreation_msg)

while True:
    schedule.run_pending()
    time.sleep(1)
