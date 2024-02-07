from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import os

root = Tk()
root.geometry('450x300')
root.title("YouTube Video Downloader")
root.configure(bg='#FCE8D8')  # Light orange background color

Label(root, text='YouTube Video Downloader', font='arial 15 bold', bg='#FCE8D8').pack()

link = StringVar()
output_path = StringVar()

Label(root, text='Paste YouTube Video Link Here:', font='arial 13 bold', bg='#FCE8D8').place(x=70, y=40)
link_enter = Entry(root, width=45, textvariable=link, bg='#FFE4E1').place(x=50, y=90)  # Light pink entry background

def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        output_path.set(directory)
        Label(root, text=f'Selected Directory: {directory}', font='arial 10', bg='#FCE8D8').place(x=50, y=150)

Button(root, text='Select Directory', font='arial 10', command=choose_directory, bg='#87CEEB').place(x=180, y=120)  # Light sky blue button

def Download():
    Label(root, text='Downloading', font='arial 13', bg='#FCE8D8').place(x=180, y=210)

    try:
        url = str(link.get())
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        
        if output_path.get():
            filename = os.path.join(output_path.get(), f'{yt.title}.mp4')
            video.download(output_path.get(), filename=filename)
            Label(root, text='Downloaded', font='arial 15', bg='#FCE8D8', fg='#228B22').place(x=180, y=210)  # Green success message
        else:
            Label(root, text='Error: Please select a directory', font='arial 15', bg='#FCE8D8', fg='#FF6347').place(x=150, y=210)  # Red error message
    except Exception as e:
        print(e)
        Label(root, text='Error downloading video', font='arial 15', bg='#FCE8D8', fg='#FF6347').place(x=150, y=210)  # Red error message

Button(root, text='Download', font='arial 15 bold', padx=2, command=Download, bg='#FF69B4').place(x=180, y=180)  # Pink button

root.mainloop()
