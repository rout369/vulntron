import requests
from lib.helper.Log import *
from lib.helper.helper import *
from lib.core import *
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from multiprocessing import Process
from queue import Queue

def log_error(message):
    """Log an error message to the console."""
    print(f"[ERROR] {message}")  # Simple logging to console

class Crawler:

    def __init__(self):
        self.visited = set()  # Use a set for faster lookups

    def get_links(self, base, proxy, headers, cookie):
        lst = []
        conn = session(proxy, headers, cookie)
        
        try:
            text = conn.get(base).text
        except requests.RequestException as e:
            log_error(f"Failed to fetch {base}: {e}")
            return lst
        
        isi = BeautifulSoup(text, "html.parser")

        for obj in isi.find_all("a", href=True):
            url = obj["href"]
            if url.startswith("http://") or url.startswith("https://"):
                continue
            elif url.startswith("mailto:") or url.startswith("javascript:"):
                continue
            elif urljoin(base, url) in self.visited:
                continue
            else:
                full_url = urljoin(base, url)
                lst.append(full_url)
                self.visited.add(full_url)  # Use a set for visited links

        return lst

    def crawl(self, base, depth, proxy, headers, level, method, cookie):
        queue = Queue()
        queue.put((base, depth))
        
        while not queue.empty():
            current_url, current_depth = queue.get()
            if current_depth < 0:
                continue
            
            urls = self.get_links(current_url, proxy, headers, cookie)
            processes = []

            for url in urls:
                p = Process(target=core.main, args=(url, proxy, headers, level, cookie, method))
                p.start()
                processes.append(p)

            for p in processes:
                p.join()

            # Enqueue the next level of URLs to crawl if depth allows
            if current_depth > 0:
                for url in urls:
                    queue.put((url, current_depth - 1))
