import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

r = requests.get('https://fincaraiz.com.co/')
soup = BeautifulSoup(r.text, 'lxml')

Element_1 = soup.find_all('div')
Element_2 = soup.find_all('div', class_='block red')
#Element_2 = soup.find_all('div',['class','block red'])
Element_3 = soup.find_all('a', limit=5, recursive=False)
#https://j2logo.com/python/web-scraping-con-python-guia-inicio-beautifulsoup/


# Sure, here are some practical tips for data scraping:

# 1. Identify the website or source from which 
# you want to scrape data.
# 2. Use a scraping tool or library that is suitable
# for the website or source you have identified.
# 3. Be mindful of the website's terms of service and any
#  legal restrictions on data scraping.
# 4. Start with small test cases to ensure your scraping
#  tool is working properly before attempting to scrape 
#  larger amounts of data.
# 5. Use headers and user agents in your scraping requests 
# to mimic a web browser and avoid being blocked by the 
# website.
# 6. Implement rate limiting to avoid overloading the 
# website and being blocked.
# 7. Store the data you scrape in a structured format 
# such as CSV, JSON, or a database.
# 8. Regularly check the website for changes that may 
# break your scraping tool and adjust accordingly.

# I hope these tips help you in your data scraping 
# journey!