import requests
import time

def downloadSites(url, session):
    with session.get(url) as response:
        print(f'Read {len(response.content)} from {url}')

def downloadAllSites(sites):
    with requests.Session() as session:
        for url in sites:
            downloadSites(url, session)
def Main():
    sites = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    startTime = time.time()
    downloadAllSites(sites)
    downloadTime = time.time() - startTime
    print(f'Download {len(sites)} in {downloadTime} time')

if __name__ == '__main__':
    Main()