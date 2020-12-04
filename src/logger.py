import pynput

from pynput.keyboard import Key, Listener, Controller

import threading

import tkinter as tk

from tkinter import filedialog, Text

import sys 

import os

from pipes import quote

from pprint import pprint

from pathlib import Path

import subprocess

from subprocess import call



keyboard = Controller()

count = 0 

keys = []



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



    with open("log.txt", "a+") as f:

        for key in keys:

            k = str(key).replace("'", "")

            if k.find("enter") > 0:

                f.write('\n')

            elif k.find("space") > 0:

                f.write(" ")

            elif k.find("Key") == -1:

                f.write(k)
            

           

def writeHeader():

    bash = "#!/bin/bash\n"

    with open("log.txt", "a+") as f:

        f.write(bash)                    

                





   

def on_release(key):

    if key == Key.f1:

        return False



    

        

def keylogger():    

    with Listener(on_press =on_press,on_release=on_release) as listener:   

        listener.join()      

    

        

      



def run():   

    threading.Thread(target=keylogger).start()

   

    

open_status = False

filename = None





def finalizeMacro():

    keyboard.press(Key.f1)

    keyboard.release(Key.f1)

    

    global open_status

    

    

        

    if open_status:

        

        with open("log.txt", "r") as file:

            data = file.read()

        

        global filename

        filename = open(open_status, 'w')

        

        filename.write(data)

        

        filename.close()

        

    

    

    else:

        

        save_as()

    os.remove("log.txt")

    

    

    return 







def save_as():

    global filename

    filename = filedialog.asksaveasfilename(defaultextension=" .*", initialdir="~", title ="Save File",filetypes=(("shell file","*.sh"), ("all files", ".")))

    with open("log.txt", "r") as file:

        data = file.read()

         

    if filename:

        

        name = filename

                

        name = name.replace("/", " ")       

                        

        filename = open(filename, 'w')

        

        filename.write(data)

        

        filename.close()    

        

def runFile(filename):

    myString = str(filename.name)

    home = str(Path.home())

    os.chdir(home)

    print(myString)

    print("PATH %s" % home)

    os.chmod('%s' % myString, 0o755)

    

    #rc = call("%s" % myString, shell = True)

        

    

    

    

    

    

    

    