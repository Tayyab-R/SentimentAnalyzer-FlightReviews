from csv import DictWriter
import csv
from bs4 import BeautifulSoup
import re

from tenacity import retry

# Open file
with open('data/doc.html', 'r') as f:
    doc = BeautifulSoup(f, 'lxml')


reviews = doc.find_all("div", class_='text_content')


def sanitize_text(text):
    """ This function clean text data. replaces special characters and unwanted strings.
        text(var:string): string var
        returns: string 
    """
    replaceables = ['Not Verified', 'Trip Verified', '✅']
    for characters in replaceables:
        text = text.replace(characters, ' ').replace('\r', '') 
    text = re.sub(r'[,."|]', '', text)
    text = text.strip()
    return text

def prepare_data(raw_data:str):
    """ Makes dictionary by splitting the data into lines"""
    reviews_list = [sanitize_text(line.get_text()) for line in raw_data]
    data = [{"reviews": review} for review in reviews_list]
    return data

    

def write_csv(file_path, data):
    """ Writes csv files of data in the form dictionaries. """
    field_name = ['reviews']
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = DictWriter(file, fieldnames=field_name, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(data)
    print("Done")
    
data = prepare_data(reviews)

# specify file output file path
file_path = 'data/output.csv'
write_csv(file_path, data)