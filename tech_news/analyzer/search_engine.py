from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    # https://www.mongodb.com/docs/manual/reference/operator/query/regex/
    regex = {"$regex": title, "$options": "i"}
    query = {"title": regex}
    result_search_news = search_news(query)
    news = []
    for new in result_search_news:
        news.append((new["title"], new["url"]))
    return news


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
