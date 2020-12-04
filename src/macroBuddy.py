#Version 3 
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
from tkinter import messagebox

keyboard = Controller()
count = 0 
keys = []

HEIGHT = 800   
WIDTH = 1000
buttons = []

global open_status
open_status = False


root = tk.Tk()
root.title("Macro Buddy")
        
canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack(fill = 'both', expand=False)

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
    
    #we make new frames to add new buttons to the side panel whenever the editor is opened 
    
    optionFrame = tk.Frame(root, bg='white',bd=5)

    optionFrame.place(relx=0.75,rely=0,relwidth=0.5, relheight=1,anchor = 'n')
    
    runButton=tk.Button(optionFrame, text="Run",font=30,bg='#46C88C',relief = "flat",borderwidth=0)

    runButton.place(relx=0.7,rely=.02, width=250, height=60, anchor = 'n')
    
    #exitFrame = tk.Frame(root, bg='#1D5A9F', bd=5)
    
    #exitFrame.place(relx = 0.9, rely = 0.75,relwidth=0.4,relheight=0.15, anchor = 'n')

    exitButton5 = tk.Button(optionFrame, text="Exit to Terminal", font=30, bg='#E06C6C', command= 
    lambda:[notepad.pack_forget(),text_scroll.pack_forget(),frame4.place_forget(),runButton.place_forget(),optionFrame.place_forget(),exitButton5.place_forget(),
    optionFrame.place_forget(),remove()],borderwidth=0)

    exitButton5.place(relx = 0.7, rely =0.75, width=250, height=60,anchor='n')
    
    
    #open new file
    def new_file():
        
        #delete what was previously written on file
        
        notepad.delete("1.0", "end")
        
        root.title("New File")
        
        #status_bar.config(text="New File     ")
        
        #make open_status false to indicate that a file hasnt been opened yet
        global open_status
        
        open_status = False

    # this add functionality to the open file button on the text editor
    
    def open_file():
        
        notepad.delete("1.0", "end")
        
        filename = filedialog.askopenfilename(initialdir="~", title= "Select File",
                                            filetypes=(("shell file","*.sh"), ("all files", "."))) 
        
        if filename:
            
            global open_status
            
            open_status = filename
        
        name = filename
        
        #status_bar.config(text=f'{name}')
        
        name.replace("/","")
        
        root.title(f'{name}')
        
        filename = open(filename, 'r')
        
        read_file = filename.read()
        
        notepad.insert("end", read_file)
        
        filename.close()


    # this add functionality to the save as button on the text editor    
    def save_as():
        filename = filedialog.asksaveasfilename(defaultextension=" .*", initialdir="~", title ="Save File",filetypes=(("shell file","*.sh"), ("all files", ".")))
        
        if filename:
            
            name = filename
            
            #status_bar.config(text=f'Saved: {name}')
            
            name = name.replace("/", " ")       
            
            root.title(f'Saved: {name}')
            
            filename = open(filename, 'w')
            
            filename.write(notepad.get("1.0","end"))
            
            filename.close()
    
    
    filename = filedialog.askopenfilename(initialdir="~", title= "Select File",
                                            filetypes=(("shell file","*.sh"), ("all files", ".")))

    # this add functionality to the save button on the text editor
    def save_file():
        global open_status
        
        if open_status:
            
            filename = open(open_status, 'w')
            
            filename.write(notepad.get("1.0","end"))
            
            filename.close()
            
            #status_bar.config(text=f'Saved: {open_status}')
            
            root.title(f'Saved: {open_status}')
        
        else:
            
            save_as()
            
    # we make a new frame4 on top of frame3 to place the text editor on frame4
    frame4 = tk.Frame(root, bg='white',bd=10)
    text_scroll = tk.Scrollbar(frame4)

    # text_scroll = tk.Scrollbar(frame2)
    text_scroll.pack(side ="left", fill = "y")
    frame4.place(relx=0,rely=0,relwidth=0.7,relheight=1,anchor='nw')

    #this is the actual text editor 
    notepad = tk.Text(frame4,font =("DejaVu Sans Mono",10), fg = "white", bg = "black",selectbackground="LightCyan2",
    selectforeground="black", insertbackground = "white",
    undo=True, yscrollcommand=text_scroll.set)
    notepad.pack(side = "left" ,fill="y")


    text_scroll.config(command=notepad.yview)

    #this is the menu for the text editor 
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
    # this exit label has commands that forget the frames originally placed at the top of this 
    # openScript function when the editor is opened so it removes those frames once exit is clicked 
    file_menu.add_command(label="Exit", command= lambda:[notepad.pack_forget(),text_scroll.pack_forget(),frame4.place_forget(),
    runButton.place_forget(),optionFrame.place_forget(),exitButton5.place_forget(),remove()])

    edit_menu = tk.Menu(notepad_menu,tearoff= False)
    notepad_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")
    edit_menu.add_command(label="Undo")
    edit_menu.add_command(label="Redo")


    #status_bar= tk.Label(root,text="ready        ", anchor='e')
    #status_bar.pack(fill="x")
    def remove():
        emptyMenu = tk.Menu(root)
        root.config(menu=emptyMenu)
        root.title("Macro Buddy")
    if filename:
            
            global open_status
            
            open_status = filename
        
    name = filename
    
    #status_bar.config(text=f'{name}')
    
    #name.replace("/","")
    
    root.title(f'{name}')
    
    filename = open(filename, 'r')
    
    read_file = filename.read()
    
    notepad.insert("end", read_file)
    
    filename.close()
    
            
def stop():
    
    return keylogger

stop = False

#this function toggles the record new macro to stop recording 

def record_toggle():
    
    global stop
    
    if stop:
        
        button5.configure(text = "Record New Macro", bg='#46C88C',activebackground = "#46C88C")
        
        stop = False
    
    else: 
        
        button5.configure(text = "Stop Recording", bg='#E06C6C',activebackground = "#E06C6C")
        
        stop = True
        
canvas.configure(bg = 'white')


# This is the frame all the way to the right where the open script button is 
frame = tk.Frame(root, bg='white',bd=5)

frame.place(relx=0.75,rely=0,relwidth=0.5, relheight=1,anchor = 'n')

button1 = tk.Button(frame, text="Open Script",font=30,fg = "white",bg='#ffbd6b', activebackground = "#ffbd6b", command= OpenScript,relief = "flat",borderwidth=0)

button1.place(relx = 0.7, rely = .02, width=250, height=60, anchor = 'n')

#---------------------------------------------------------------------------------------------------------

# This is the frame for the lower right start recording

#frame3 = tk.Frame(root, bg='#1D5A9F',bd=10)

#frame3.place(relx = 0.9, rely = 0.6,relwidth=0.4,relheight=0.3, anchor = 'n')

#the button for the frame3 on the lower right

button5 = tk.Button(frame, text="Record New Macro", font=30,fg = "white", bg='#46C88C', activebackground = "#46C88C", 
command = record_toggle,relief = "flat")

button5.place(relx = 0.7, rely =0.75, width=250, height=60,anchor='n')



#-----------------------------------------------------------------------------------------------

# This is the frame for the main big window in the center where the terminal will go 
frame2 = tk.Frame(root, bg='white',bd=10)

frame2.place(relx=0,rely=0,relwidth=0.7,relheight=1,anchor='nw')

#this is the gray label inside frame2

label2 = tk.Label(frame2)

label2.place(relwidth=1, relheight=1)

#this is where we embed the terminal into the GUI 

wid = label2.winfo_id()
    
try:
    
    p = subprocess.Popen(
        
        ["xterm","-into", str(wid), "-geometry", "113x65"],
        
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)

#throw an exception if xterm is not installed

except FileNotFoundError:
    
    showwarning("Error", "xterm is not installed")


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        print(p.poll())
        p.terminate()
        print(p.poll())
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
    
root.mainloop()
