import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
# URL = "https://www.empireonline.com/movies/features/best-movies-2/"   # The actual website hides the title information. Tags of h3 are no longer visible.

# Write your code below this line 👇

response = requests.get(URL)
response.raise_for_status()
data = response.text
soup = BeautifulSoup(data, "html.parser")
print(soup.prettify())

h3s = soup.select("h3")

titles = []
index = len(h3s) - 1
while index >= 0:
    titles.append(h3s[index].getText())
    index -= 1


with open("day45_beautiful-soup/100-movies-to-watch/movies.txt", "w") as f:
    for title in titles:
        f.write(f"{title}\n")
