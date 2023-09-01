from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    # https://www.mongodb.com/docs/manual/reference/operator/query/regex/
    regex = {"$regex": title, "$options": "i"}
    query = {"title": regex}

    return get_result_news(query)


# Requisito 8
def search_by_date(date):
    try:
        # https://blog.betrybe.com/desenvolvimento-web/dd-mm-aaaa-como-formatar-data/#2
        # Primeiro tem que mudar o date de str para objeto datetime.
        obj_date = datetime.strptime(date, "%Y-%m-%d")
        new_date_format = obj_date.strftime("%d/%m/%Y")

        regex = {"$regex": new_date_format}
        query = {"timestamp": regex}

        return get_result_news(query)
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    regex = {"$regex": category, "$options": "i"}
    query = {"category": regex}

    return get_result_news(query)


def get_result_news(query):
    result_search_news = search_news(query)
    news = []
    for new in result_search_news:
        news.append((new["title"], new["url"]))

    return news
