from bs4 import BeautifulSoup
import requests
import telegram
from monitor.models import Monitor
from datetime import datetime, timedelta

URL = "https://search.naver.com/search.naver?where=blog&sm=tab_opt&query=민병철유폰&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=so%3Add%2Ca%3Aall%2Cp%3Aall"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

bot = telegram.Bot(token ='1677998245:AAHnoqqsn9DWhIqhJ1AGODooOE-CS6iPKLo')

def run():

  row, _ = Monitor.objects.filter(created_at__lte=datetime.now() - timedelta(days=7)).delete()
  
  for item in soup.select("div > a.api_txt_lines.total_tit")[0:10]:
      title = item.get_text()
      link = item.get("href")

      if '민병철' in title:
        if (Monitor.objects.filter(link__iexact=link).count() == 0):
            Monitor(title=title, link=link).save()
            bot.sendMessage(-1001480449951, '{} {}'.format(title, link))
