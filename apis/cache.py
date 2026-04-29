cache = {}

def get_data(url):
    if url in cache:
        print("From cache")
        return cache[url]
    
    import requests
    res = requests.get(url)
    cache[url] = res.text
    return res.text