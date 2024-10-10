import requests
from lib.helper.Log import *
from lib.helper.helper import *
from lib.core import *
from bs4 import BeautifulSoup
from multiprocessing import Process, Manager
from urllib.parse import urljoin
from queue import Queue
import time

class Crawler:
    @classmethod
    def get_links(cls, base, proxy, headers, cookie, visited):
        lst = []  # List to store found URLs
        local_visited = set()  # Use a local set to track visited URLs for this call

        conn = session(proxy, headers, cookie)
        try:
            response = conn.get(base, timeout=10)
            response.raise_for_status()  # Raise an error for bad responses
            text = response.text
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {base}: {e}")
            return lst
        
        isi = BeautifulSoup(text, "html.parser")

        for obj in isi.find_all("a", href=True):
            url = obj["href"]

            # Skip mailto and javascript links
            if url.startswith("mailto:") or url.startswith("javascript:"):
                continue

            # Join relative URLs with the base URL
            full_url = urljoin(base, url)

            # Use the Manager list for membership checking
            if full_url in visited:
                continue

            # Allow only URLs that start with the base URL or are relative
            if full_url.startswith(base) or "://" not in full_url:
                lst.append(full_url)
                local_visited.add(full_url)  # Track in the local set

        # Update the global visited list at the end
        for url in local_visited:
            visited.append(url)  # Append each URL to the Manager list

        return lst

    @classmethod
    def crawl(cls, base, depth, proxy, headers, level, method, cookie):
        manager = Manager()
        cls.visited = manager.list()  # Use a Manager list for shared access across processes

        urls = cls.get_links(base, proxy, headers, cookie, cls.visited)

        for url in urls:
            if url.startswith(("https://", "http://")):
                p = Process(target=core.main, args=(url, proxy, headers, level, cookie, method))
                p.start()
                
                if depth != 0:
                    p.join()  # Wait for the current process to complete before crawling deeper
                    cls.crawl(url, depth - 1, proxy, headers, level, method, cookie)
                else:
                    break  # Break if max depth is reached
            time.sleep(1)  # Adding a delay to avoid overwhelming the server
# def log_error(message):
#     """Log an error message to the console."""
#     print(f"[ERROR] {message}")  # Simple logging to console

# class Crawler:

#     def __init__(self):
#         self.visited = set()  # Use a set for faster lookups

#     def get_links(self, base, proxy, headers, cookie):
#         lst = []
#         conn = session(proxy, headers, cookie)
        
#         try:
#             text = conn.get(base).text
#         except requests.RequestException as e:
#             log_error(f"Failed to fetch {base}: {e}")
#             return lst
        
#         isi = BeautifulSoup(text, "html.parser")

#         for obj in isi.find_all("a", href=True):
#             url = obj["href"]
#             if url.startswith("http://") or url.startswith("https://"):
#                 continue
#             elif url.startswith("mailto:") or url.startswith("javascript:"):
#                 continue
#             elif urljoin(base, url) in self.visited:
#                 continue
#             else:
#                 full_url = urljoin(base, url)
#                 lst.append(full_url)
#                 self.visited.add(full_url)  # Use a set for visited links

#         return lst

#     def crawl(self, base, depth, proxy, headers, level, method, cookie):
#         queue = Queue()
#         queue.put((base, depth))
        
#         while not queue.empty():
#             current_url, current_depth = queue.get()
#             if current_depth < 0:
#                 continue
            
#             urls = self.get_links(current_url, proxy, headers, cookie)
#             processes = []

#             for url in urls:
#                 p = Process(target=core.main, args=(url, proxy, headers, level, cookie, method))
#                 p.start()
#                 processes.append(p)

#             for p in processes:
#                 p.join()

#             # Enqueue the next level of URLs to crawl if depth allows
#             if current_depth > 0:
#                 for url in urls:
#                     queue.put((url, current_depth - 1))

            
