import threading
import sys
import requests
import os

#Function to download a file from the url 
def download_file(url, destination):
    response = requests.get(url)
     # Save the content of the response to a local file
    with open(destination, 'wb') as f:
        f.write(response.content)
        
 #Function to download files sequentially       
def sequential_download(urls):
    for i, url in enumerate(urls):
        # Generate a file name
        filename = f"file_{i}.dat"
        download_file(url,filename)

#Function use to dowload files with multithreading
def multithread_download(urls):
    threads = []
    for i, url in enumerate(urls):
        filename = f"file_{i}.dat"
        thread = threading.Thread(target=download_file, args=(url, filename))
        thread.start()
        # Keep track of the thread
        threads.append(thread)
    
    for thread in threads:
        thread.join()
        
if __name__=="__main__":
    urls = sys.argv[1:]
    if not urls:
        print("Please add at least one URL as a command line argument.")
        sys.exit()