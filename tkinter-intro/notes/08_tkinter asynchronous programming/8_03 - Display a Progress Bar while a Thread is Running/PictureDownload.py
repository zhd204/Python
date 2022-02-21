import requests
from threading import Thread


class PictureDownload(Thread):
    def __init__(self, url):
        super().__init__()

        self.picture_file = None
        self.url = url

    def run(self):
        """ download a picture and save it to a file """

        # download the picture
        response = requests.get(self.url)
        picture_name = self.url.split('/')[-1]
        # picture_file = f"./assets/{picture_name}.jpg"
        picture_file = f"tkinter-intro/notes/08_tkinter asynchronous programming/8_03 - Display a Progress Bar while a Thread is Running/assets/{picture_name}.jpg"

        # save the picture to a file
        # https://docs.python.org/3/library/functions.html#open
        # default mode for open is text read, use rb or wb for non-text file such as images
        with open(picture_file, 'wb') as f:
            f.write(response.content)

        self.picture_file = picture_file
