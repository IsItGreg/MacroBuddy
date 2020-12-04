#Version 3 

import tkinter as tk
from tkinter import filedialog, Text
import subprocess
from tkinter.messagebox import showwarning
from tkinter import font
import re
from code import InteractiveConsole
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
#import logger

HEIGHT = 1000
WIDTH = 1000

global open_status
open_status = False
filename = None

root = tk.Tk()
root.title("Macro Buddy")
        
canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack(fill = 'both', expand=True)
    
def OpenScript():
    
    #we make new frames to add new buttons to the side panel whenever the editor is opened 
    global filename
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

    # this add functionality to the open file button on the text editor
    
    def open_file():
        
        notepad.delete("1.0", "end")
        global filename
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


    # this add functionality to the save as button on the text editor    
    def save_as():
        global filename
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

    # this add functionality to the save button on the text editor
    def save_file():
        global filename
        global open_status
        
        if open_status:
            
            filename = open(open_status, 'w')
            
            filename.write(notepad.get("1.0","end"))
            
            filename.close()
            
            status_bar.config(text=f'Saved: {open_status}')
            
            root.title(f'Saved: {open_status}')
        
        else:
            
            save_as()
            
    # we make a new frame4 on top of frame3 to place the text editor on frame4
    frame4 = tk.Frame(root, bg='#dbf6e9',bd=5)
    text_scroll = tk.Scrollbar(frame4)

    # text_scroll = tk.Scrollbar(frame2)
    text_scroll.pack(side ="right", fill = "y")
    frame4.place(relx=0.1,rely=0.1,relwidth=0.6,relheight=0.8,anchor='nw')

    #this is the actual text editor 
    notepad = tk.Text(frame4,font =("DejaVu Sans Mono",10), selectbackground="LightCyan2",selectforeground="black",undo=True, yscrollcommand=text_scroll.set)
    notepad.pack(side = "right" ,fill="y")


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
    file_menu.add_command(label="Exit", command= lambda:[notepad.pack_forget(),text_scroll.pack_forget(),frame4.place_forget(),runButton.place_forget(),optionFrame.place_forget(),exitButton5.place_forget(),exitFrame.place_forget(),remove()])

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
        emptyMenu = FrameMenu
        root.config(menu=emptyMenu)
        
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
    



toggle = False

#this function toggles the record new macro to stop recording 

def record_toggle():
    global toggle
    
    
        
    if toggle:
        
        button5.configure(text = "Record New Macro")
        
        toggle = False
            
    else: 
               
        button5.configure(text = "Stop Recording")        
        
        toggle = True
        
    
               
canvas.configure(background = 'gray')


# This is the frame all the way to the right where the openscript button is 
frame = tk.Frame(root, bg='#dbf6e9',bd=5)

frame.place(relx=0.9,rely=0.1,relwidth=0.4, relheight=0.6,anchor = 'n')

button1 = tk.Button(frame, text="Open Script",font=30,bg='#9ddfd3', command= OpenScript)

button1.place(relx = 0.37, relwidth=0.70,relheight=0.1, anchor = 'n')



#---------------------------------------------------------------------------------------------------------

# This is the frame for the lower right start recording

frame3 = tk.Frame(root, bg='#9ddfd3',bd=5)

frame3.place(relx = 0.9, rely = 0.75,relwidth=0.4,relheight=0.15, anchor = 'n')

#the button for the frame3 on the lower right

button5 = tk.Button(frame3, text="Record New Macro", font=30, bg='#9ddfd3', command = record_toggle)

button5.place(relx = 0.37,relwidth=0.8,relheight=0.90,anchor='n')



#-----------------------------------------------------------------------------------------------

# This is the frame for the main big window in the center where the terminal will go 
frame2 = tk.Frame(root, bg='#9ddfd3',bd=5)

frame2.place(relx=0.1,rely=0.1,relwidth=0.6,relheight=0.8,anchor='nw')

#this is the gray label inside frame2






#this is where we embed the terminal into the GUI 

wid = frame2.winfo_id()
    
try:
    
    p = subprocess.Popen(
        
        ["xterm","-into", str(wid), "-geometry", "87x60"],
        
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    

#throw an exception if xterm is not installed

except FileNotFoundError:
    
    showwarning("Error", "xterm is not installed")


FrameMenu = tk.Menu(root)
FrameMenu.add_command(label="Open Script", command = OpenScript)
FrameMenu.add_command(label="Record", command = record_toggle)
FrameMenu.add_command(label="Run")
root.config(menu = FrameMenu)
    
root.mainloop()
