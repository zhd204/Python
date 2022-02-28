import requests


class Post:
    def __init__(self):
        response = requests.get(url="https://api.npoint.io/22badedfea9003ca4a21")
        response.raise_for_status()
        self.data = response.json()

    def get_blogs(self):
        return self.data


# post = Post()
# data = post.get_blogs()
# print(type(data[0]["id"]))
# print(data)