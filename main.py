from bs4 import BeautifulSoup
import requests as req

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

res = req.get(url)
res.raise_for_status()
html = res.text

soup = BeautifulSoup(html, "html.parser")

title_tags = soup.find_all(name="h3", class_="title")
titles = [tag.getText() for tag in title_tags]
titles.reverse()

print(titles)

with open("movies.txt", "w") as f:
    for title in titles:
        f.write(f"{title}\n")
