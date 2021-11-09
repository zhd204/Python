# https://www.pythontutorial.net/tkinter/tkinter-thread-progressbar/
from PictureDownload import PictureDownload
from App import App

if __name__ == '__main__':
    # url = 'https://source.unsplash.com/random/640x480'
    # download = PictureDownload(url)
    # download.start()
    # download.join()
    # print("finished")
    app = App(640, 480)
    app.mainloop()
