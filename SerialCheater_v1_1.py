import serial,time
import numpy as np
from tkinter import *
import codecs
import tkinter as tk
import os

root = Tk()
root.geometry('500x370')
root.title("Vitaly SERIAL-Cheater v1.1")
root.configure(bg='black')

GREEN = "#00ff00"
global File_data
global string
ID = 0
transSTAT=0
input_HEX=True

text= Text(root, width= 50, height= 30, borderwidth=0,selectbackground=GREEN, selectforeground='black', background="black",foreground=GREEN,highlightthickness=2,highlightbackground="green", highlightcolor= GREEN, font=("Consolas", 11))
text.config(state=DISABLED)
text.place(x=10,y=10,width=480,height=280)

text_draft= Text(root, width= 50, height= 30, borderwidth=0,blockcursor=True,insertbackground=GREEN,selectbackground=GREEN, selectforeground='black', background="black",foreground=GREEN,highlightthickness=2,highlightbackground="green", highlightcolor= GREEN, font=("Consolas", 11))
text_draft.place(x=500,y=10,width=857,height=650)

text_label1 = tk.Label(root, text="COM-Port",
                 bg='black', fg="green", pady=10, padx=10, font=("Consolas", 11)) 
text_label1.place(x=10,y=390,width=150,height=30)

COM = tk.StringVar()
COM_entry = tk.Entry(root, textvariable=COM, selectbackground=GREEN, selectforeground='black',insertbackground=GREEN, borderwidth=0, background="black",foreground=GREEN,highlightthickness=2,highlightbackground="green", highlightcolor= GREEN,bg='black', font=("Consolas", 11))
COM_entry.insert(0, "COM1")
COM_entry.place(x=10,y=420,width=150,height=30)


text_label2 = tk.Label(root, text="Baudrate",
                 bg='black', fg="green", pady=10, padx=10, font=("Consolas", 11)) 
text_label2.place(x=175,y=390,width=150,height=30)

baudrate = tk.StringVar()
baudrate_entry = tk.Entry(root, textvariable=baudrate, selectbackground=GREEN, selectforeground='black',insertbackground=GREEN, borderwidth=0, background="black",foreground=GREEN,highlightthickness=2,highlightbackground="green", highlightcolor= GREEN,bg='black', font=("Consolas", 11))
baudrate_entry.insert(0, "9600")
baudrate_entry.place(x=175,y=420,width=150,height=30)

text_label2 = tk.Label(root, text="Delay",
                 bg='black', fg="green", pady=10, padx=10, font=("Consolas", 11)) 
text_label2.place(x=340,y=390,width=150,height=30)

time = tk.StringVar()
time_entry = tk.Entry(root, textvariable=time, selectbackground=GREEN, selectforeground='black',insertbackground=GREEN, borderwidth=0, background="black",foreground=GREEN,highlightthickness=2,highlightbackground="green", highlightcolor= GREEN,bg='black', font=("Consolas", 11))
time_entry.insert(0, "1000")
time_entry.place(x=340,y=420,width=150,height=30)
time_var=1000

ser = serial.Serial(
    port=COM.get(),
    baudrate=baudrate_entry.get(),
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    xonxoff=False
)

def read_file():
    global string
    global File_data
    global input_HEX
    try:
        with open('message.txt', 'r') as file:
            File_data = file.read().rstrip()
            if input_HEX == True:
                hex_str = File_data
                # convert hex string to ASCII string
                string = ''.join(chr(int(i, 16)) for i in hex_str.split())
            else:
                string = File_data
    except:
        text.config(state=NORMAL)
        text.insert(INSERT,'\n')
        text.insert(INSERT,'Suspicious message format... -_-')
        text.insert(INSERT,'\n')
        text.see("end")
        text.config(state=DISABLED)

isExist = os.path.exists('message.txt')
if isExist == False:
    with open('message.txt', 'w') as f:
        f.write('Enter your message here...')

read_file()

isExist = os.path.exists('drafts.txt')
if isExist == False:
    with open('drafts.txt', 'w') as f:
        f.write('Write here your commands to save...')
        text_draft.insert(INSERT,'Write here your commands to save...')
else:
    with open('drafts.txt', 'r') as file:
        Draft_data = file.read().rstrip()        
        text_draft.insert(INSERT,Draft_data)
text_draft.see("end")

ENTRY = tk.StringVar()
ENTRY_entry = tk.Entry(root, textvariable=ENTRY, selectbackground=GREEN, selectforeground='black',insertbackground=GREEN, borderwidth=0, background="black",foreground=GREEN,highlightthickness=2,highlightbackground="green", highlightcolor= GREEN,bg='black', font=("Consolas", 11))
ENTRY_entry.insert(0, File_data)
ENTRY_entry.place(x=10,y=297,width=480,height=30)

def fun():
     global text
     global transSTAT
     text.config(state=NORMAL)     
     text.insert(INSERT,'>Broadcast ')
     if transSTAT == True:
          text.insert(INSERT,'stopped')
          text.insert(INSERT,'\n')
          text.see("end")
          transSTAT=False
     else:
          text.insert(INSERT,'started')
          text.insert(INSERT,'\n')
          text.see("end")
          transSTAT=True
     text.config(state=DISABLED)
 
def fun2():
    global time_var
    text.config(state=NORMAL)
    try:
        ser.port=COM.get()
        ser.baudrate=baudrate_entry.get()
        time_var=time.get()
        text.insert(INSERT,'>Variables set:')
        text.insert(INSERT,'\n')
        text.insert(INSERT,'COM Port: ')
        text.insert(INSERT,COM.get())
        text.insert(INSERT,'\n')
        text.insert(INSERT,'BaudRate: ')
        text.insert(INSERT,baudrate_entry.get())
        text.insert(INSERT,'\n')
        text.insert(INSERT,'Delay: ')
        text.insert(INSERT,time_var)
        text.insert(INSERT,'\n')
        text.insert(INSERT,'\n')
        text.see("end")
    except:
        text.insert(INSERT,'.txt file ERROR')
        text.insert(INSERT,'\n')
        text.see("end")
    text.config(state=DISABLED)

def save():
    with open('drafts.txt', "w") as output_file:
        text_for_save = text_draft.get(1.0, tk.END)
        output_file.write(text_for_save)    
    text.config(state=NORMAL)
    text.insert(INSERT,'\n')
    text.insert(INSERT,'Your file has been successfully saved!')
    text.insert(INSERT,'\n')
    text.see("end")
    text.config(state=DISABLED)

def input_format():
    global input_HEX
    text.config(state=NORMAL)
    text.insert(INSERT,'\n')
    text.insert(INSERT,'>Message format set: ')   
    if input_HEX == False:
        b5.config(text = "[HEX]")
        text.insert(INSERT,'Hexadecimal')
        input_HEX=True
    else:
        b5.config(text = "[ASCII]")
        text.insert(INSERT,'ASCII')
        input_HEX=False
    text.insert(INSERT,'\n')
    text.insert(INSERT,'\n')
    text.see("end")
    text.config(state=DISABLED)
        
b1 = Button(root,text = "Broadcast",font=("Consolas", 11),command = fun, relief='flat',fg=GREEN,bg='black',activeforeground = GREEN,activebackground = "black",borderwidth=0,pady=10)  
b1.place(x=175,y=331,width=150,height=30)

b2 = Button(root,text = "Apply",font=("Consolas", 11),command = fun2, relief='flat',fg=GREEN,bg='black',activeforeground = GREEN,activebackground = "black",borderwidth=0,pady=10)  
b2.place(x=175,y=450,width=150,height=30)

b4 = Button(root,text = "Save",font=("Consolas", 11),command = save, relief='flat',fg=GREEN,bg='black',activeforeground = GREEN,activebackground = "black",borderwidth=0,pady=10)  
b4.place(x=1207,y=667,width=150,height=30)

b5 = Button(root,text = "[HEX]",font=("Consolas", 11),command = input_format, relief='flat',fg=GREEN,bg='black',activeforeground = GREEN,activebackground = "black",borderwidth=0,pady=10)  
b5.place(x=340,y=331,width=150,height=30)


def send_mes():
     global text
     global transSTAT
     global ID
     ID=ID+1
     global ENTRY
     global string
     text.config(state=NORMAL)     
     text.insert(INSERT, "Message ")
     text.insert(INSERT, ID)
     text.insert(INSERT,'\n')
     try:
         ser.write(str.encode(string))
         text.insert(INSERT, File_data)
     except:
         text.insert(INSERT,'Send ERROR')
     text.insert(INSERT,'\n')
     text.insert(INSERT,'\n')
     text.see(END)
     text.config(state=DISABLED)
    
def loop():
     global transSTAT
     global ENTRY
     global time_var
     with open('message.txt', 'w') as f:
         f.write(ENTRY.get())    
     if transSTAT == True:
         read_file()
         send_mes()
         b1.config(text = "<Broadcast>")
     else:
         b1.config(text = "Broadcast")
     root.after(time_var, loop)


def fun3():
     global text
     global transSTAT
     text.config(state=NORMAL)
     text.insert(INSERT,'>Single message sent... ')
     text.see("end")
     text.config(state=DISABLED)
     transSTAT=False
     read_file()
     send_mes()
      
b3 = Button(root,text = "Single",font=("Consolas", 11),command = fun3, relief='flat',fg=GREEN,bg='black',activeforeground = GREEN,activebackground = "black",borderwidth=0,pady=10)  
b3.place(x=10,y=331,width=150,height=30)

ENTRY_entry.focus_set()
root.after(1000, loop)
root.mainloop()
