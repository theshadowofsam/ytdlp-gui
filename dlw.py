"""
Samuel Lee
dlw.py
1/3/2022

gui for dlp.py
"""
import tkinter as tk
import dlp

class DLP():
    def __init__(self):
        self.window = tk.Tk()


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
        url = self.entry_main.get()
        dl = dlp.start([url])
        if dl != 0:
            self.label_main['text'] = 'ERROR'
        else:
            self.label_main['text'] = 'DONE!'


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = DLP()
    app.draw()
    app.run()