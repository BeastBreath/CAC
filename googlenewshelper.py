from GoogleNews import GoogleNews


def getNewsTitles(search_query):
    search_query: str
    
    # Setting up google news variable
    googlenews = GoogleNews(encode='utf-8')
    googlenews.search(search_query)

    # Getting result JSON object
    result = googlenews.result()

    # Getting titles
    titles = list()
    for article in result:
        titles.append(article["media"])

    print("START")
    print(titles)
    return titles

getNewsTitles("APPL")