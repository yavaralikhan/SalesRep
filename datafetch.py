from bs4 import BeautifulSoup
import requests


url = 'https://www.worldfootball.net/teams/barcelona_3/2019/3/'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
print(soup.title.text)
# print(soup.body.prettify())
# print(soup.body.text)

divData = soup.find('div', class_='box')
# print(divData.text)

table = divData.find_all('tr')
file = open('barcelona_2018-19.csv', 'w', encoding='UTF-8')

# data = []
for tr in table:
    # print(tr.text.strip())
    d = tr.text.split()
    # print(tr.text.split())
    # data.append(d)
    ds = ','.join(d)
    file.write(ds)
    file.write('\n')


file.close()
# print(data)
