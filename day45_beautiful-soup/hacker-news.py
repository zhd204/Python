from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/"
response = requests.get(url)
response.raise_for_status()
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

ls = soup.select(".titlelink, .score")
titles = []
index = 0
# for item in ls:
#     print(item.get("class"))
while index < len(ls) - 1:
    title = ls[index].getText()
    link = ls[index].get("href")
    if ls[index + 1].get("class")[0].lower() == "score":
        upvote = int(ls[index + 1].getText().split(" ")[0])
        index += 2
    else:
        upvote = 0
        index += 1
    titles.append((title, link, upvote))
    print((title, link, upvote))

highest_upvote = 0
highest_upvote_index = 0

for i in range(len(titles)):
    if titles[i][2] >= highest_upvote:
        highest_upvote = titles[i][2]
        highest_upvote_index = i

print(f"\n{titles[highest_upvote_index][0]} has {titles[highest_upvote_index][2]} upvotes.\n Its link is {titles[highest_upvote_index][1]}")