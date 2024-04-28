import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/'

# Write your code below this line 👇

response = requests.get(URL)
movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")

articles = soup.find_all(name="h3", class_="title")

movie_title = []
for article_tags in articles:
    title = article_tags.getText()
    movie_title.append(title)
sorted_title_lists = movie_title[::-1]
with open("movies.txt", mode="w", encoding="utf-8") as f:
    for titles in sorted_title_lists:
        f.write(f"{titles}\n")