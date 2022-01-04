"""
Samuel Lee
dlw.py
1/3/2022

gui for dlp.py
"""
from multiprocessing import Process
import tkinter as tk
import dlp

class DLP():
    def __init__(self):
        self.window = tk.Tk()
        self.dl = None
        self.is_downloading = False


    def draw(self):
        self.label_main = tk.Label(
            master=self.window,
            text="Enter a youtube URL",
            width=100,
            height=2
            )
        self.entry_main = tk.Entry(
            master=self.window,
            width=100
            )
        self.button_main = tk.Button(
            master=self.window,
            text="Download",
            width=20,
            height=2,
            command=self.download
        )
        self.label_main.pack()
        self.entry_main.pack()
        self.button_main.pack()

        
    def download(self):
        if self.is_downloading:
            return
        url = self.entry_main.get()
        self.dl = Process(target=dlp.start, args=([url],), daemon=False)
        self.dl.start()
        self.is_downloading = True
        self.label_main['text'] = "Downloading..."
        self.window.after(150, self.downloading)
        # self.dl = dlp.start([url])


    def downloading(self):
        if self.is_downloading:
            if self.dl.exitcode == None:
                self.window.after(150, self.downloading)
                return
            else:
                self.label_main['text'] = "Done!"
                self.is_downloading = False
        else:
            return


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = DLP()
    app.draw()
    app.run()