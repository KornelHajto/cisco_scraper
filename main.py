import sys

import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
req = requests.get(url).text
parse = BeautifulSoup(req)
print(parse.prettify())
# So we need to use req with bs4.
