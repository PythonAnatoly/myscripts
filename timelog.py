#!/usr/bin/env python3.4

from tkinter import *
from tkinter import ttk
import datetime
import time

def get_path(): return 'ToDoLog.csv'


def get_time(Activities, Comments):
    last_line = ''
    while last_line == '':
        try:
            s = open(get_path(), 'r', encoding='utf-8')
            last_line = s.readlines()[-1]
            s.close()
        except FileNotFoundError as error: # creating file if one don't exist
            f = open(get_path(), 'x', encoding='utf8')
            f.write('{0}\n{1};;;;\n'.format('Date and Time;Spent Time;Activity;Comments/Results;', time.strftime("%A %d %b %Y %X", time.localtime()) ) )
            f.close()
    
    time_str = [n for n in last_line.split(';')][0].split(' ')[4] # extracting time from the file's last string
    
    t = time.localtime()

    current_time = datetime.timedelta(hours=t.tm_hour, minutes=t.tm_min, seconds=t.tm_sec)

    ts = time_str
    last_time = datetime.timedelta(hours=int(ts[0:2]), minutes=int(ts[3:5]), seconds=int(ts[6:]))
    
    spent_time = current_time - last_time
    
    write_csv(spent_time, Activities, Comments)
    
def write_csv(spent_time, Activities, Comments):
    timing = open(get_path(), 'a', encoding='utf-8')
    timing.write('{0};{1};{2};{3};\n'.format(time.strftime("%A %d %b %Y %X", time.localtime()), str(spent_time), Activities, Comments ))
    timing.close()
    
def get_text(Activities_get, Comments_get, Activities, Comments):
    get_time(Activities, Comments)
    Comments_get.delete(0, END)
    Activities_get.delete(0, END)
    fcs()
    
def enter(event):
    A = Activities.get()
    C = Comments.get()
    get_time(A, C)
    Comments.delete(0, END)
    Activities.delete(0, END)
    fcs()
           
root = Tk()
root.title("To Do Tracker")
root.geometry("700x200")

app = Frame(root)
app.grid()

text1 = StringVar()
text2 = StringVar()
text3 = StringVar()

# Labels
lb0 = ttk.Label(app, text="{0:20}".format('')).grid(column=1, row=1, sticky=W)
lb1 = ttk.Label(app, text="Describe shortly what you did:").grid(column=2, row=1, sticky=W)
lb2 = ttk.Label(app, text="Comments:").grid(column=3, row=1, sticky=W)

# Entries
Activities = ttk.Combobox(app, textvariable=text3)
Activities.grid(column=2, row=2, sticky=(W, E))
Activities['values'] = ('Python', 'English', 'housework')
def fcs(): Activities.focus()
fcs()

Comments = ttk.Entry(app, width=50, textvariable=text2)
Comments.grid(column=3, row=2, sticky=(W, E))

# Activities = ttk.Entry(app, width=30, textvariable=text1)
# Activities.grid(column=2, row=2, sticky=(W, E))


bttn1 = Button(app, text = 'Save&Clean', command=lambda: get_text(Activities, Comments, Activities.get(), Comments.get()))
bttn1.grid(column=4, row=2)

Activities.bind('<Return>',enter)
Comments.bind('<Return>',enter)

Activities.bind("<Control-s>",enter)
Comments.bind("<Control-s>",enter)


root.mainloop()

