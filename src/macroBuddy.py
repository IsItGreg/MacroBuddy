#Working Version

import os

import tkinter as tk

from tkinter import filedialog, Text,  messagebox

import subprocess

from tkinter.messagebox import showwarning

from tkinter import font

import re

from code import InteractiveConsole

from contextlib import redirect_stderr, redirect_stdout

from io import StringIO

from pathlib import Path

from subprocess import call

from pathlib import Path

#import logger



HEIGHT = 1000

WIDTH = 1000



selected = False

global open_status

open_status = False

filename = None

p = None

work_dir = os.path.dirname(__file__)

hist_path = "history.sh"

rc_path = "bashrc.txt"

histfile = os.path.join(work_dir, hist_path)

rcfile = os.path.join(work_dir, rc_path)



root = tk.Tk()

root.title("Macro Buddy")

        

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)

canvas.pack(fill = 'both', expand=True)





def OpenScript():

    

    global filename



    #we make new frames to add new buttons to the side panel whenever the editor is opened 

    

    optionFrame = tk.Frame(root, bg='#383b3d',bd=5)



    runButton=tk.Button(optionFrame, text="Run",font=30,bg='#007ACC',fg ="white", command= runfile)



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

    notepad = tk.Text(frame4,font =("DejaVu Sans Mono",12),insertbackground="white", bg = "#1E1E1E",fg ="white",selectbackground="#C9DEF5",selectforeground="white",undo=True, yscrollcommand=text_scroll.set)

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

    file_menu.add_command(label="Run", command= runfile)

    file_menu.add_separator()

    # this exit label has commands that forget the frames originally placed at the top of this 

    # openScript function when the editor is opened so it removes those frames once exit is clicked 

    file_menu.add_command(label="Exit", command= lambda:[notepad.pack_forget(),text_scroll.pack_forget(),frame4.place_forget(),runButton.place_forget(),optionFrame.place_forget(),exitButton5.place_forget(),remove()])



    edit_menu = tk.Menu(notepad_menu,bg ="#252526",fg ="white",relief ="flat",tearoff= False)

    notepad_menu.add_cascade(label="Edit", menu=edit_menu)

    edit_menu.add_command(label="Cut")

    edit_menu.add_command(label="Copy")

    edit_menu.add_command(label="Paste")

    edit_menu.add_command(label="Undo")

    edit_menu.add_command(label="Redo")





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

def runfile():

    global filename

    #filename = filedialog.askopenfilename(initialdir=work_dir, title= "Select File",

    #                                        filetypes=(("shell file","*.sh"), ("all files", "."))) 



    myString = str(filename.name)

    home = str(Path.home())

    os.chdir(home)

    os.chmod('%s' % myString, 0o755)

    #os.system("x-terminal-emulator -e 'bash -c \"source %s; exec bash\"'" % myString)

    rc = call("%s" % myString, shell = True)



def saveHistory():

    with open(histfile, "r") as file:

        data = file.read()

        print(data)

    

    

    global filename



    filename = filedialog.asksaveasfilename(defaultextension=" .*", initialdir="~", title ="Save File",filetypes=(("shell file","*.sh"), ("all files", ".")))   



    if filename:





        name = filename



        name = name.replace("/", " ")       



        filename = open(filename, 'w')

       

        filename.write(data)

       

        filename.close()



        os.remove(histfile)    







#this function toggles the record new macro to stop recording 

def record_toggle():

    global toggle

    global p

    

        

    if toggle:

        

        button5.configure(text = "Record New Macro", bg='#68217A',activebackground = "#68217A")

        p.kill()

        saveHistory()

        toggle = False

    

            

    else: 

               

        button5.configure(text = "Stop Recording", bg='#F35F25',activebackground = "#F35F25")      

        toggle = True

        open(histfile, 'a+').close()

            

            

        try:

            p = subprocess.Popen(

            ["xterm", "-into", str(wid), "-geometry", "113x76", "-bg","#1E1E1E", "-fa","DejaVu Sans Mono", "-fs","11", "-e", "bash --rcfile " + rcfile + " -i"],

            stdin=subprocess.PIPE, stdout=subprocess.PIPE)



        except FileNotFoundError:

            showwarning("Error", "xterm failed to load")



               

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

    



def on_closing():

    global p

    if messagebox.askokcancel("Quit", "Do you want to quit?"):

        if p is not None:

            p.kill()    

        root.destroy()







FrameMenu = tk.Menu(root,bg ="#252526",fg ="white",relief ="flat")

FrameMenu.add_command(label="Open Script", command = OpenScript)

FrameMenu.add_command(label="Record", command = record_toggle)

FrameMenu.add_command(label="Run", command= runfile)

root.config(menu = FrameMenu)



root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

