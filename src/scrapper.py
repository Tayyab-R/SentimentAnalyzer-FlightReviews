from bs4 import BeautifulSoup

# Open file
with open('doc.html', 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')


title = doc.title

review_tag = doc.find_all(class_='text_content')

for review in review_tag:
    text = review.get_text()
    with open('reviews.txt', 'a') as f:
        f.write(text.strip())

print('Done')