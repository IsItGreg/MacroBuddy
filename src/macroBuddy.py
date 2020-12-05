import sys

import os

import tkinter as tk

from tkinter import filedialog, Text

import threading

import pynput

from pynput.keyboard import Key, Listener, Controller

import subprocess

from tkinter.messagebox import showwarning

from tkinter import font

import re

from code import InteractiveConsole

from contextlib import redirect_stderr, redirect_stdout

from io import StringIO


keyboard = Controller()

count = 0 

keys = []


HEIGHT = 1000

WIDTH = 1000

buttons = []


global open_status
global p
open_status = False
work_dir = os.path.dirname(__file__)
hist_path = "history.txt"
rc_path = "bashrc.txt"
histfile = os.path.join(work_dir, hist_path)
rcfile = os.path.join(work_dir, rc_path)


root = tk.Tk()

root.title("Macro Buddy")

        

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)

canvas.pack(fill = 'both', expand=True)


def on_press(key):

    

    global keys, count

    

    keys.append(key)

    

    count += 1

    

    print("{0} pressed".format(key))

    

    if count >= 1:

        

        count = 0

        

        write_file(keys)

        

        keys = []


def write_file(keys):

    

    with open("log.txt", 'a') as f:

        

        for key in keys:

            

            k = str(key).replace("'", "")

            

            if k.find("enter") > 0:

                

                f.write('\n')

                

            elif k.find("space") > 0:

                

                f.write(" ")

                

            elif k.find("Key") == -1:

                

                f.write(k)

    


    

def on_release(key):

    

    if key == Key.esc:

        

        return False

        

def keylogger():

    

    with Listener(on_press =on_press,on_release=on_release) as listener: 

        

        def stopRec():

            

            print("hello")

            

            listener.stop()

            

        listener.join()

        

        return stopRec

        


def run():

    

    threading.Thread(target=keylogger).start()

    



def record():

    

    run()



    

 

def OpenScript():

    

    optionFrame = tk.Frame(root, bg='#dbf6e9',bd=5)


    optionFrame.place(relx=0.9,rely=0.1,relwidth=0.4, relheight=0.6,anchor = 'n')

    

    runButton=tk.Button(optionFrame, text="Run",font=30,bg='#9ddfd3')


    runButton.place(relx=0.37,rely=0.2,relwidth=0.7,relheight=0.1, anchor = 'n')

    

    exitFrame = tk.Frame(root, bg='#dbf6e9', bd=5)

    

    exitFrame.place(relx = 0.9, rely = 0.75,relwidth=0.4,relheight=0.15, anchor = 'n')


    exitButton5 = tk.Button(exitFrame, text="Exit to Terminal", font=30, bg='#9ddfd3', command= lambda:[notepad.pack_forget(),text_scroll.pack_forget(),frame4.place_forget(),runButton.place_forget(),optionFrame.place_forget(),exitButton5.place_forget(),exitFrame.place_forget(),remove()])


    exitButton5.place(relx = 0.37,relwidth=0.8,relheight=0.90,anchor='n')

    

    

    #open new file

    def new_file():

        

        #delete what was previously written on file

        

        notepad.delete("1.0", "end")

        

        root.title("New File")

        

        status_bar.config(text="New File     ")

        

        #make open_status false to indicate that a file hasnt been opened yet

        global open_status

        

        open_status = False


    def open_file():

        

        notepad.delete("1.0", "end")

        

        filename = filedialog.askopenfilename(initialdir="~", title= "Select File",

                                            filetypes=(("shell file","*.sh"), ("all files", "."))) 

        

        if filename:

            

            global open_status

            

            open_status = filename

        

        name = filename

        

        status_bar.config(text=f'{name}')

        

        name.replace("/","")

        

        root.title(f'{name}')

        

        filename = open(filename, 'r')

        

        read_file = filename.read()

        

        notepad.insert("end", read_file)

        

        filename.close()



        

    def save_as():

        filename = filedialog.asksaveasfilename(defaultextension=" .*", initialdir="~", title ="Save File",filetypes=(("shell file","*.sh"), ("all files", ".")))

        

        if filename:

            

            name = filename

            

            status_bar.config(text=f'Saved: {name}')

            

            name = name.replace("/", " ")       

            

            root.title(f'Saved: {name}')

            

            filename = open(filename, 'w')

            

            filename.write(notepad.get("1.0","end"))

            

            filename.close()

    

    

    filename = filedialog.askopenfilename(initialdir="~", title= "Select File",

                                            filetypes=(("shell file","*.sh"), ("all files", ".")))


    

    def save_file():

        global open_status

        

        if open_status:

            

            filename = open(open_status, 'w')

            

            filename.write(notepad.get("1.0","end"))

            

            filename.close()

            

            status_bar.config(text=f'Saved: {open_status}')

            

            root.title(f'Saved: {open_status}')

        

        else:

            

            save_as()

            


    frame4 = tk.Frame(root, bg='#dbf6e9',bd=5)

    text_scroll = tk.Scrollbar(frame4)


    # text_scroll = tk.Scrollbar(frame2)

    text_scroll.pack(side ="right", fill = "y")

    frame4.place(relx=0.1,rely=0.1,relwidth=0.6,relheight=0.8,anchor='nw')


    #text box

    notepad = tk.Text(frame4,font =("DejaVu Sans Mono",10), selectbackground="LightCyan2",selectforeground="black",undo=True, yscrollcommand=text_scroll.set)

    notepad.pack(side = "right" ,fill="y")



    text_scroll.config(command=notepad.yview)


    #menu

    notepad_menu = tk.Menu(root)

    root.config(menu = notepad_menu)


    file_menu = tk.Menu(notepad_menu,tearoff=False)

    notepad_menu.add_cascade(label="File", menu = file_menu)

    file_menu.add_command(label="New", command = new_file)

    file_menu.add_command(label="Open", command=open_file)

    file_menu.add_command(label="Save", command = save_file)

    file_menu.add_command(label="Save As", command= save_as)

    file_menu.add_command(label="Run")

    file_menu.add_separator()

    file_menu.add_command(label="Exit", command= lambda:[notepad.pack_forget(),text_scroll.pack_forget(),frame4.place_forget(),runButton.place_forget(),optionFrame.place_forget(),remove()])


    edit_menu = tk.Menu(notepad_menu,tearoff= False)

    notepad_menu.add_cascade(label="Edit", menu=edit_menu)

    edit_menu.add_command(label="Cut")

    edit_menu.add_command(label="Copy")

    edit_menu.add_command(label="Paste")

    edit_menu.add_command(label="Undo")

    edit_menu.add_command(label="Redo")



    status_bar= tk.Label(root,text="ready        ", anchor='e')

    status_bar.pack(fill="x")

    def remove():

        emptyMenu = tk.Menu(root)

        root.config(menu=emptyMenu)

        root.title(text = "Macro Buddy")

    if filename:

            

            global open_status

            

            open_status = filename

        

    name = filename

    

    status_bar.config(text=f'{name}')

    

    name.replace("/","")

    

    root.title(f'{name}')

    

    filename = open(filename, 'r')

    

    read_file = filename.read()

    

    notepad.insert("end", read_file)

    

    filename.close()

    

            

def stop():

    

    return keylogger


stop = False


def record_toggle():

    

    global stop
    global p
    

    if stop:

        
	
        button5.configure(text = "Record New Macro")
        p.kill()
    

        try:

    

            p = subprocess.Popen(

        

            ["xterm", "-into", str(wid), "-geometry", "87x60", "-e", "bash --rcfile " + rcfile + " -i"],

        

            stdin=subprocess.PIPE, stdout=subprocess.PIPE)


        except FileNotFoundError:

    

            showwarning("Error", "xterm is not installed")
        

        stop = False

    

    else: 

        

        button5.configure(text = "Stop Recording")
        open(histfile, 'w').close()

        stop = True

        

canvas.configure(background = 'gray')



# This is the frame all the way to the right where the stop and consolidate logs buttons are 

frame = tk.Frame(root, bg='#dbf6e9',bd=5)


frame.place(relx=0.9,rely=0.1,relwidth=0.4, relheight=0.6,anchor = 'n')


button1 = tk.Button(frame, text="Open Script",font=30,bg='#9ddfd3', command= OpenScript)


button1.place(relx = 0.37, relwidth=0.70,relheight=0.1, anchor = 'n')


#button3 = tk.Button(frame, text="Open Terminal", font=30,bg='#9ddfd3')


#button3.place(relx=0.37,rely=0.4,relwidth=0.7,relheight=0.1, anchor = 'n')


#---------------------------------------------------------------------------------------------------------


# This is the frame for the lower right start recording


frame3 = tk.Frame(root, bg='#dbf6e9',bd=5)


frame3.place(relx = 0.9, rely = 0.75,relwidth=0.4,relheight=0.15, anchor = 'n')


button5 = tk.Button(frame3, text="Record New Macro", font=30, bg='#9ddfd3', command = record_toggle)


button5.place(relx = 0.37,relwidth=0.8,relheight=0.90,anchor='n')




#-----------------------------------------------------------------------------------------------


# This is the frame for the main big window in the center where the terminal will go 

frame2 = tk.Frame(root, bg='#dbf6e9',bd=5)


frame2.place(relx=0.1,rely=0.1,relwidth=0.6,relheight=0.8,anchor='nw')


label2 = tk.Label(frame2)


label2.place(relwidth=1, relheight=1)


wid = label2.winfo_id()

    

try:

    

    p = subprocess.Popen(

        

        ["xterm", "-into", str(wid), "-geometry", "87x60", "-e", "bash --rcfile " + rcfile + " -i"],

        

        stdin=subprocess.PIPE, stdout=subprocess.PIPE)


except FileNotFoundError:

    

    showwarning("Error", "xterm is not installed")


    

root.mainloop()


