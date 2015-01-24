#!/usr/bin/env python3.4

from tkinter import *
from tkinter import ttk
import datetime
import time

def get_time(Activities, Comments):
    path1 = '\Python34\storagetime.txt'
    source = open(path1, encoding='utf-8')
    s = source.read()
    source.close()
    
    if '\ufeff' in s:
        s = s.replace('\ufeff', '') # if BOM remove BOM from file

    t = time.localtime()

    current_time = datetime.timedelta(hours=t.tm_hour, minutes=t.tm_min, seconds=t.tm_sec)

    last_time = datetime.timedelta(hours=int(s[0:2]), minutes=int(s[3:5]), seconds=int(s[6:]))
    
    spent_time = current_time - last_time
    
    write_csv(spent_time, Activities, Comments)
    
    print(spent_time)
    
    source = open(path1, 'w', encoding='utf8')
    source.write(time.strftime("%X", time.localtime()))
    source.close()
    
def write_csv(spent_time, Activities, Comments):
    path2 = r'c:\Dropbox\timing.csv'
    timing = open(path2, 'a', encoding='utf-8')
    timing.write('{0};{1};{2};{3};\n'.format(time.strftime("%A %d %b %Y %X", time.localtime()), str(spent_time), Activities, Comments ))
    timing.close()
    
def get_text(ent1, ent2, Activities, Comments):
    get_time(Activities, Comments)
    ent1.delete(0, END)
    ent2.delete(0, END)
    
root = Tk()
root.title("Time Log")
root.geometry("700x400")

app = Frame(root)
app.grid()

text1 = StringVar()
text2 = StringVar()

lb1 = ttk.Label(app, text="Activity").grid(column=1, row=1, sticky=W)
lb2 = ttk.Label(app, text="Comments").grid(column=2, row=1, sticky=W)

Activities = ttk.Entry(app, width=20, textvariable=text1)
Activities.grid(column=1, row=2, sticky=(W, E))

Comments = ttk.Entry(app, width=60, textvariable=text2)
Comments.grid(column=2, row=2, sticky=(W, E))
   
bttn1 = Button(app, text = 'Save&Clean', command=lambda: get_text(Activities, Comments, Activities.get(), Comments.get()))
bttn1.grid(column=2, row=3)

root.mainloop()










