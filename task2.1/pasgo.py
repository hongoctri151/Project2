from bs4 import BeautifulSoup
import requests
import re
import csv

#element store
locate = []
title  =[]
img = []
rate = []

def crawl(link,number):
    page = requests.get(link+number)
    soup = BeautifulSoup(page.content,"html.parser")
    infomations = soup.findAll("div",class_="wapitem")
    #select infor from item
    for infomation in infomations:
        locate.append(infomation.find('p',class_='text-address notranslate').text)
        title.append(infomation.find('img').attrs['alt'])
        img.append(infomation.find("img").attrs['src'])
        rate.append(infomation.find('input',class_='rating rating-sao form-control hide').attrs['value'])

    # # #condition stop
    if len(title) > 1000:
        return 0
    elif int(number)>18:
        return 0
    else:
        return crawl(link,str(int(number)+1))


## Load trang web, tách theo các thẻ tag như html
links = [
    'https://pasgo.vn/tim-kiem?search=n%C6%B0%E1%BB%9Bng=',
    'https://pasgo.vn/tim-kiem?search=buffet=',
    'https://pasgo.vn/tim-kiem?search=l%E1%BA%A9u=',
    'https://pasgo.vn/tim-kiem?search=h%E1%BA%A3i%20s%E1%BA%A3n=',
    'https://pasgo.vn/tim-kiem?search=buffet=',
    'https://pasgo.vn/tim-kiem?search=L%E1%BA%A9u='
]
for link in links:
    crawl(link,"1")

with open('data_pasgo.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['Title','Locate','Rate','Link_image'])
	for i in range(len(title)):
		writer.writerow([title[i],locate[i],rate[i],img[i]])
