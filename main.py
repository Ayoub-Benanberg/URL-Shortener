import pyshorteners
from tkinter import *

def shortner():
    url = urlInput.get()
    shortLink = pyshorteners.Shortener()
    try:
        short_url = shortLink.tinyurl.short(url)
        shortUrlOutput.delete(0, END)
        shortUrlOutput.insert(0, short_url)
    except Exception as e:
        shortUrlOutput.delete(0, END)
        shortUrlOutput.insert(0, "Error shortening URL")

def copy_btn():
    root.clipboard_clear()
    root.clipboard_append(shortUrlOutput.get())
    root.update()

root = Tk()
root.title("URL Shortener")
root.geometry("400x400")

urlLabel = Label(root, text="Enter Votre URL:")
urlLabel.grid(column=0,row=0,pady=10)

urlInput = Entry(root, width=50)
urlInput.grid(column=0,row=1,padx=20,pady=5)

shortenButton = Button(root, text="Shorten URL", command=shortner)
shortenButton.grid(column=0,row=2,pady=10)

shortUrlLabel = Label(root, text="Shortened URL:")
shortUrlLabel.grid(column=0,row=3,pady=10)

shortUrlOutput = Entry(root, width=50)
shortUrlOutput.grid(column=0,row=4,pady=20)

copyButton = Button(root, text="Copy", command=copy_btn)
copyButton.grid(column=1,row=4)

root.mainloop()