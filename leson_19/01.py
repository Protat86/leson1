from bs4 import BeautifulSoup
import requests

# URL сайту
url = 'https://news.ycombinator.com/'

# Отримати контент
content = requests.get(url).content

# Створити екземпляр soup
soup = BeautifulSoup(content, 'html.parser')

# Знайти всі заголовки статей
headlines = soup.find_all('a', class_='storylink')

# Надрукувати заголовки на консолі
for index, headline in enumerate(headlines):
    print(f"{index + 1}. {headline.text}")
