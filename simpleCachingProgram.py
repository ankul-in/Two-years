#caching using python
cache={}
def get_data_from_internet(url):
    #idk man 
    return None
def caching(url):
    if cache.get(url):
        return cache[url]
    else:
        data=get_data_from_internet(url)
        cache[url]=data
        return data
