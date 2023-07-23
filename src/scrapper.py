from bs4 import BeautifulSoup

# Open file
with open('data/doc.html', 'r') as f:
    doc = BeautifulSoup(f, 'lxml')


title = doc.title
print(title)

review_tag = doc.find_all("div", class_='text_content')

for review in review_tag:
    text = review.get_text()
    with open('data/reviews.txt', 'a') as f:
        f.write(text.strip())

print('Done')