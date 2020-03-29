from tkinter import *
import tkinter as tk
from tkinter import filedialog 
import os
import shutil

def to_file(y):
    path=y
    basename = os.path.basename(path) 
    print(basename)
    os.system(' mv '+path+ ' /home/ananya/Documents/Projects/Detectx-Yolo-V3/video.avi')
    os.system('python detect_video.py')
    quit()
    os.remove('video.avi')

def to_call():
    file_path = filedialog.askopenfilename()
    to_file(file_path)

root = tk.Tk()

root.title("REAL TIME OBJECT DETECTION IN VIDEO USING YOLO-V3")

HEIGHT=457.5
WIDTH=817.5
canvas=tk.Canvas(root, height=HEIGHT, width=WIDTH).pack()

background_image=tk.PhotoImage(file='preview.png')
background_label= tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

myButton= Button(root, text="SELECT VIDEO FILE",font="Time 15",padx=40, pady=80, bg='#e0e0d1',fg='#b30059', bd=3, command= to_call).place(relx=0.6,rely=0.7,relwidth=0.3,relheight=0.1)

root.mainloop()

 
