from typing import cast
from bs4 import BeautifulSoup
from bs4.element import PreformattedString
import requests
import re
import csv
comment = []
rate = []
def crawNewsData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    items = soup.findAll('div',class_='card__imageContainer')
    links = [item.find('a').attrs['href'] for item in items]
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        gird = soup.find('div',class_='recipe-reviewed-items recipe-reviewed-items--grid')
        if gird != None:
            evaluates = gird.findAll('div',class_='component ugc-review ugc-item recipe-review-wrapper')
            for evaluate in evaluates:
                point = evaluate.find('span',class_='review-star-text').text.strip()
                point = re.sub(r'\D', "",point)
                rate.append(point)
                comment_text = evaluate.find('span',class_='recipe-review-body--truncated').text.strip()
                comment.append(comment_text)
        

links = [
    'https://www.allrecipes.com/',
    'https://www.allrecipes.com/recipes/187/holidays-and-events/christmas/',
    'https://www.allrecipes.com/recipes/23070/everyday-cooking/cookware-and-equipment/air-fryer/',
    'https://www.allrecipes.com/recipes/78/breakfast-and-brunch/',
    'https://www.allrecipes.com/recipes/76/appetizers-and-snacks/',
    'https://www.allrecipes.com/recipes/201/meat-and-poultry/chicken/',
    'https://www.allrecipes.com/recipes/471/meat-and-poultry/beef/ground/',
    'https://www.allrecipes.com/recipes/473/main-dish/burgers/hamburgers/',
    'https://www.allrecipes.com/recipes/253/everyday-cooking/slow-cooker/',
    'https://www.allrecipes.com/recipes/94/soups-stews-and-chili/'
]
for link in links:
    crawNewsData(link)

with open('allrecipes.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['rate',"Comment"])
	for i in range(len(rate)):
		writer.writerow([rate[i],comment[i]])
