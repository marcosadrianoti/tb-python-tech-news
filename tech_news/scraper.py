import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_link = selector.css("a.next::attr(href)").get()
    if next_link:
        return next_link
    return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author > a::text").get()
    reading_time = int(
        selector.css("li.meta-reading-time::text").re_first(r"\d+")
    )
    summary = (
        selector.css("div.entry-content > p:first-of-type")
        .xpath("string()")
        .get()
        .strip()
    )
    category = selector.css("a.category-style > span.label::text").get()
    print(category)
    new = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }
    return new


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    news_list = []

    while len(news_list) < amount:
        news_list.extend(scrape_updates(fetch(url)))
        url = scrape_next_page_link(fetch(url))

    list_by_amount = [news_list[i] for i in range(amount)]

    scraped = []
    for news_item in list_by_amount:
        scraped_news = scrape_news(fetch(news_item))
        scraped.append(scraped_news)

    create_news(scraped)

    return scraped
