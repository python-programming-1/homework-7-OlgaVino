import datetime
import os
import requests
from bs4 import BeautifulSoup

today_date = datetime.date.today()
day_delta = datetime.timedelta(days=1)
prev_date = today_date - day_delta

url = 'https://www.gocomics.com/pearlsbeforeswine/'

for i in range(10):
    every_day = (today_date - i*day_delta)
    every_day_string = every_day.strftime('%Y/%m/%d')

    today_url = url+every_day_string
    comics = requests.get(today_url)
    comics.raise_for_status()
    print(comics.status_code)
    soup = BeautifulSoup(comics.text, 'html.parser')
    pic_div = soup.select('div .item-comic-image')
    pic_url = pic_div[0].contents[0].attrs['src'] + '.png'
    picture = requests.get(pic_url)
    picture.raise_for_status()
    print(pic_url)

    recent_image = open(os.path.basename(pic_url), 'wb')
    for chunk in picture.iter_content(100000):
        recent_image.write(chunk)

    recent_image.close()






