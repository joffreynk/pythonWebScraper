import requests
from bs4 import BeautifulSoup
 
 # Getting page HTML through request
page = requests.get('https://people.com/celebrity/') 
# Parsing content using beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser') 
 
# Initialize List of celebraties
celebraties = []

