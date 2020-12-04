

import tkinter as tk
from tkinter import filedialog, Text,  messagebox
import subprocess
from tkinter.messagebox import showwarning
from tkinter import font
import re
from code import InteractiveConsole
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import logger

HEIGHT = 1000
WIDTH = 1000

global open_status
open_status = False
filename = None
global selected
selected = False

root = tk.Tk()
root.title("Macro Buddy")
        
canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack(fill = 'both', expand=True)
    
def OpenScript():
    
    global filename

    #we make new frames to add new buttons to the side panel whenever the editor is opened 
    
    optionFrame = tk.Frame(root, bg='#383b3d',bd=5)

    runButton=tk.Button(optionFrame, text="Run",font=30,bg='#007ACC',fg ="white",command = lambda:[logger.runFile(filename)])

    exitButton5 = tk.Button(optionFrame, text="Exit to Terminal", font=30, bg='#68217A',fg ="white", activebackground = "#68217A", 
    command= lambda:[notepad.pack_forget(),text_scroll.pack_forget(),status_bar.pack_forget(),
    frame4.place_forget(),runButton.place_forget(),optionFrame.place_forget(),exitButton5.place_forget(),remove()])

    
    
    
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

    def cut_text(e):    
        global selected
        
        if e:
            selected = root.clipboard_get()
        else:
            if notepad.selection_get():
                selected = notepad.selection_get()
                notepad.delete("sel.first", "sel.last")
                root.clipboard_clear()
                root.clipboard_append(selected)


    def copy_text(e):
        global selected
        
        if e:
            selected = root.clipboard_get()
        if notepad.selection_get():
            selected = notepad.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected)

    def paste_text(e):
        global selected
        
        if e:
            selected = root.clipboard_get()
        else:
            if selected:
                position = notepad.index(tk.INSERT)
                notepad.insert(position, selected)
    
    
    optionFrame.place(relx=0.75,rely=0,relwidth=0.5, relheight=1,anchor = 'n')
    runButton.place(relx=0.7,rely=0.02,width=250,height=60, anchor = 'n')
    exitButton5.place(relx = 0.7, rely =0.75, width=250, height=60,anchor='n')

    # we make a new frame4 on top of frame3 to place the text editor on frame4
    frame4 = tk.Frame(root, bg='#383b3d',bd=10)
    text_scroll = tk.Scrollbar(frame4)

    # text_scroll = tk.Scrollbar(frame2)
    text_scroll.pack(side ="left", fill = "y")
    frame4.place(relx=0,rely=0,relwidth=0.7,relheight=.98,anchor='nw')

    #this is the actual text editor 
    notepad = tk.Text(frame4,font =("DejaVu Sans Mono",12), bg = "#1E1E1E",fg ="white",insertbackground="white",selectbackground="#C9DEF5",selectforeground="white",undo=True, yscrollcommand=text_scroll.set)
    notepad.pack(side = "left" , fill="y")


    text_scroll.config(command=notepad.yview)

    #this is the menu for the text editor 
    notepad_menu = tk.Menu(root,bg ="#252526",fg ="white",relief ="flat")
    root.config(menu = notepad_menu)

    file_menu = tk.Menu(notepad_menu,bg ="#252526",fg ="white",relief ="flat",tearoff=False)
    notepad_menu.add_cascade(label="File", menu = file_menu)
    file_menu.add_command(label="New", command = new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command = save_file)
    file_menu.add_command(label="Save As", command= save_as)
    file_menu.add_command(label="Run", command = lambda:[logger.runFile(filename)])
    file_menu.add_separator()
    # this exit label has commands that forget the frames originally placed at the top of this 
    # openScript function when the editor is opened so it removes those frames once exit is clicked 
    file_menu.add_command(label="Exit", command= lambda:[notepad.pack_forget(),text_scroll.pack_forget(),frame4.place_forget(),runButton.place_forget(),optionFrame.place_forget(),exitButton5.place_forget(),remove()])

    edit_menu = tk.Menu(notepad_menu,bg ="#252526",fg ="white",relief ="flat",tearoff= False)
    notepad_menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut", command= lambda: cut_text(False), accelerator = "(Ctrl+x)")
    edit_menu.add_command(label="Copy", command= lambda: copy_text(False), accelerator = "(Ctrl+c)")
    edit_menu.add_command(label="Paste      ", command= lambda: paste_text(False), accelerator = "(Ctrl+v)")
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo", command= notepad.edit_undo, accelerator = "(Ctrl+z)")
    edit_menu.add_command(label="Redo", command= notepad.edit_redo, accelerator = "(Ctrl+y)")


    status_bar= tk.Label(root,text="ready        ", bg ="#252526",fg ="white",relief ="flat",anchor='e')
    status_bar.pack(fill="x")
    def remove():
        emptyMenu = FrameMenu
        root.title("Macro Buddy")
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
    
    root.bind('<Control-Key-x>', cut_text)
    root.bind('<Control-Key-c>', copy_text)
    root.bind('<Control-Key-v>', paste_text)
    
    



toggle = False

#this function toggles the record new macro to stop recording 

def record_toggle():
    global toggle
    
    
        
    if toggle:
        
        
        button5.configure(text = "Record New Macro", bg='#68217A',activebackground = "#68217A")
        logger.finalizeMacro()
        toggle = False
            
    else: 
               
        button5.configure(text = "Stop Recording", bg='#F35F25',activebackground = "#F35F25")      
        logger.run()
        logger.writeHeader()
        toggle = True
        
    
               
canvas.configure(bg = '#383b3d')


# This is the frame all the way to the right where the open script button is 
frame = tk.Frame(root, bg='#383b3d',bd=5)

frame.place(relx=0.75,rely=0,relwidth=0.5, relheight=1,anchor = 'n')

button1 = tk.Button(frame, text="Open Script",font=30,fg = "white",bg='#007ACC', activebackground = "#007ACC", command= OpenScript,relief = "flat",borderwidth=0)

button1.place(relx = 0.7, rely = .02, width=250, height=60, anchor = 'n')

#---------------------------------------------------------------------------------------------------------

# This is the frame for the lower right start recording

#frame3 = tk.Frame(root, bg='#1D5A9F',bd=10)

#frame3.place(relx = 0.9, rely = 0.6,relwidth=0.4,relheight=0.3, anchor = 'n')

#the button for the frame3 on the lower right

button5 = tk.Button(frame, text="Record New Macro", font=30,fg = "white", bg='#68217A', activebackground = "#68217A", 
command = record_toggle,relief = "flat")

button5.place(relx = 0.7, rely =0.75, width=250, height=60,anchor='n')

#-----------------------------------------------------------------------------------------------

# This is the frame for the main big window in the center where the terminal will go 
frame2 = tk.Frame(root, bg='#383b3d',bd=10)

frame2.place(relx=0,rely=0,relwidth=0.7,relheight=1,anchor='nw')

#this is the gray label inside frame2

label2 = tk.Label(frame2)

label2.place(relwidth=1, relheight=1)

#this is where we embed the terminal into the GUI 

wid = label2.winfo_id()

    
try:
    
    p = subprocess.Popen(
        
        ["xterm","-into", str(wid), "-geometry", "113x76","-bg","#1E1E1E", "-fa","DejaVu Sans Mono", "-fs","11"],
        
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)

#throw an exception if xterm is not installed

except FileNotFoundError:
    
    showwarning("Error", "xterm is not installed")


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        print(p.poll())
        #p.terminate()
        print(p.poll())
        root.destroy()



FrameMenu = tk.Menu(root,bg ="#252526",fg ="white",relief ="flat")
FrameMenu.add_command(label="Open Script", command = OpenScript)
FrameMenu.add_command(label="Record", command = record_toggle)
FrameMenu.add_command(label="Run", command = lambda:[logger.runFile(filename)])
root.config(menu = FrameMenu)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
