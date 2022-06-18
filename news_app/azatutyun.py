from requests_html import HTMLSession
from datetime import datetime


def get_news_azatutyun():
    url = 'https://www.azatutyun.am/news'

    session = HTMLSession()

    r = session.get(url=url)

    news_list = list()

    for news in r.html.find('.fui-grid__inner'):

        single_news_dict = {
            'news_site_name': news.base_url.split('.')[1].title(),
            'news_url': list(news.absolute_links)[0],
            'news_date': news.text.split('\n', 1)[0],
            'news_text': news.text.split('\n', 1)[1].replace('\n', ' '),
            'update_time': datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        }
        news_list.append(single_news_dict)

    return news_list
