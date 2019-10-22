'''
Problem: URL shortener
Implement a URL shortener with the following methods:

•	shorten(url):
  which shortens the url into a six-character alphanumeric string,such as zLg6wl.

•	restore(short):
  which expands the shortened string into the original url.
  If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
'''
import random
import math

class URLShortener:
  shortened = {}
  original = {}
  SHORT_BASE = 'https://sh.url/'
  SHORT_LEN = 6
  AVALABLE_SHORT_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

  def shorten(self, url):
    short_id = self.original.get(url, '')
    while len(short_id) != self.SHORT_LEN:
      for _ in range(self.SHORT_LEN):
        random_index = math.floor(random.uniform(0, len(self.AVALABLE_SHORT_CHARS)))
        short_id += self.AVALABLE_SHORT_CHARS[random_index]
      if not self.shortened.get(short_id, None):
        short_id == ''
    self.shortened[short_id] = url
    self.original[url] = short_id
    return self.SHORT_BASE + short_id

  def restore(self, short):
    short_id = short[len(short)-6: len(short)]
    original = self.shortened.get(short_id, None)
    if original:
      return original
    else:
      return None
  
  # def 

urls = URLShortener()
print("SHORTEN:", 'https://www.google.com', "->", urls.shorten('https://www.google.com'))
print("SHORTEN:", 'https://www.microsoft.com', "->", urls.shorten('https://www.microsoft.com'))
print("SHORTEN:", 'https://www.google.com', "->", urls.shorten('https://www.google.com'))

print("RESTORE:", urls.shorten('https://www.google.com'), "->", urls.restore(urls.shorten('https://www.google.com')))
