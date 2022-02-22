import requests


class Post:
    def __init__(self):
        response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
        response.raise_for_status()
        self.data = response.json()

    def get_blogs(self):
        return self.data


post = Post()
data = post.get_blogs()
print(type(data[0]["id"]))