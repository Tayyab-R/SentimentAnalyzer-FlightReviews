from urllib import response
from bs4 import BeautifulSoup
import bs4
import requests



links_list = ['https://www.airlinequality.com/airline-reviews/british-airways/?sortby=post_date%3ADesc&pagesize=100',
              'https://www.airlinequality.com/airline-reviews/british-airways/page/2/?sortby=post_date%3ADesc&pagesize=100', 
              'https://www.airlinequality.com/airline-reviews/british-airways/page/3/?sortby=post_date%3ADesc&pagesize=100']

def get_html_docs(links_list):
    """ Gets HTML pages and parse it. 
        'links_list'(list) : Pass list of links to scrap.
    """
    for links in links_list:
        site = requests.get(links)
        soup = BeautifulSoup(site.text, 'lxml')
        with open('data/doc.html', 'a') as f:
           f.write(soup.prettify()) 
    print('Done...')
    
    
get_html_docs(links_list)

