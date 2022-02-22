from bs4 import BeautifulSoup

with open("day45_beautiful-soup/website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")
title_tag = soup.title
print(title_tag)
print(title_tag.name)
print(title_tag.string)

h1_tag = soup.h1    # first h1 tag
print(h1_tag)
print(h1_tag["id"])

a_tag = soup.a  # first anchor tag
print(soup.a)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(f"\n{tag}")
    print(tag.string, tag.text, tag.getText())
    print(tag["href"], tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

print("\nusing css syntax\n")
anchor = soup.select_one(selector="p a")
print(anchor)

name = soup.select_one(selector="#name")   # use # for id
print(name)

headings = soup.select_one(selector=".heading")     # use . for class
print(headings)
