import requests
from bs4 import BeautifulSoup
 
 # Getting page HTML through request
page = requests.get('https://people.com/celebrity/') 
# Parsing content using beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser') 
 
# Initialize List of celebraties
celebraties = []

file = open('celebraties')

links = soup.select("#tax-sc__recirc-list_1-0 a") 
for anchor in links:
    text = anchor.select(' .card__content .card__title .card__title-text')[0].text
    category = anchor.select(' .card__content')[0]['data-tag']
    writer = anchor.select('.card__content .mntl-card__byline')[0]['data-byline']
    imgURL = anchor.select('.loc.card__top .card__media.mntl-universal-image.card__media.universal-image__container .img-placeholder img')[0]['data-src']
    
