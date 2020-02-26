import requests
from bs4 import BeautifulSoup

import openpyxl

url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=0&as-type=HISTORY'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

mobile = soup.find_all('div', class_='_3wU53n')
rating = soup.find_all('div',class_='hGSR34')
price = soup.find_all('div',class_='_1vC4OE _2rQ-NK')

m_list =[]
for item in mobile:
    m_list.append(item.text)

r_list=[]
for r in rating:
    r_list.append(r.text)


p_list=[]
for p in price:
    p_list.append(p.text) 
 
final = list(zip(m_list, r_list, p_list))

print(final)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Mobile detail"
sheet['A1'] = 'Mobile Name'
sheet['B1'] = 'Rating'
sheet['C1'] = 'Price'

for item in final:
    sheet.append(item)

wb.save('mobile1.xlsx')