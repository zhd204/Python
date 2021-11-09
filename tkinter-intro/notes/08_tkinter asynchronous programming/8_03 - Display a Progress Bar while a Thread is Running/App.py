import tkinter as tk
from tkinter import ttk
from PictureDownload import PictureDownload
from PIL import ImageTk, Image


class App(tk.Tk):

    def __init__(self, canvas_width, canvas_height):
        super().__init__()
        self.resizable(0, 0)
        self.title('Image Viewer')
        self.attributes('-topmost', 1)

        # progress frame
        self.progress_frame = ttk.Frame(self)

        # configure the grid to place the progress bar is at the center
        # self.progress_frame.columnconfigure(0, weight=1)
        # self.progress_frame.rowconfigure(0, weight=1)

        # progressbar
        self.pb = ttk.Progressbar(self.progress_frame, orient=tk.HORIZONTAL, mode='indeterminate')
        self.pb.grid(row=0, column=0, sticky=tk.EW, padx=10, pady=10)

        # place the progressbar frame
        self.progress_frame.grid(row=0, column=0, sticky=tk.NSEW)

        # picture frame
        self.picture_frame = ttk.Frame(self)

        # canvas width and height
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        # canvas
        self.canvas = tk.Canvas(self.picture_frame, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(row=0, column=0)

        # place the picture frame
        self.picture_frame.grid(row=0, column=0)

        # next button
        btn = ttk.Button(self, text='Next Picture')
        btn['command'] = self.handle_download
        btn.grid(row=1, column=0)

    def start_downloading(self):
        self.progress_frame.tkraise()
        self.pb.start(20)

    def stop_downloading(self):
        self.picture_frame.tkraise()
        self.pb.stop()

    # def set_picture(self, file_path):
    #     """ Set the picture to the canvas """
    #     pil_img = Image.open(file_path) # use PIL package. tk.PhotoImage only works with .gif
    #
    #     # resize the picture
    #     # resized_img = pil_img.resize(
    #     #     (self.canvas_width, self.canvas_height),
    #     #     Image.ANTIALIAS)
    #
    #     self.img = ImageTk.PhotoImage(pil_img)
    #
    #     # set background image
    #     self.canvas.create_image(
    #         0,
    #         0,
    #         anchor=tk.NW,
    #         image=self.img)

    def set_picture(self, file_path):
        """ Set the picture to the canvas """
        img = Image.open(file_path) # use PIL package. tk.PhotoImage only works with .gif
        self.img = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img) # use self.img, not img (local variable)

    def monitor(self, download_thread):
        """ monitor the download thread"""
        if download_thread.is_alive():
            self.after(100, lambda: self.monitor(download_thread))
        else:
            self.stop_downloading()
            self.set_picture(download_thread.picture_file)

    def handle_download(self):
        """ download a random photo from unsplash """
        self.start_downloading()
        url = 'https://source.unsplash.com/random/640x480'
        download_thread = PictureDownload(url)
        download_thread.start()

        self.monitor(download_thread)
