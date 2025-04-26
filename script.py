import threading
import sys
import requests
import os

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as f:
        f.write(response.content)
        
def sequential_download(urls):
    for i, url in enumerate(urls):
        filename = f"file_{i}.dat"
        download_file(url,filename)

def multithread_download(urls):
    threads = []
    for i, url in enumerate(urls):
        filename = f"file_{i}.dat"
        thread = threading.Thread(target=download_file, args=(url, filename))
        thread.start()
        threads.append(thread)