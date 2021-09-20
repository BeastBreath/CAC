from GoogleNews import GoogleNews


def getNewsTitles(search_query):
    search_query: str
    
    # Setting up google news variable
    googlenews = GoogleNews(encode='utf-8')
    googlenews.search(search_query)

    # Getting result JSON object
    results = googlenews.result()

    # Getting titles and media (Maybe use date and give more recent more credibility)
    articles = list()
    for result in results:
        articles.append({result["title"], result["media"]})

    return articles

getNewsTitles("APPL")