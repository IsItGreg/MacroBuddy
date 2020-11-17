# MacroBuddy
Project for Software Engineering 1 at UMass Lowell




How to Run Macro Buddy (PROTOTYPE V1)
======


Go to src folder and clone the code or copy and paste it,  make sure python3 is installed in your system.

### Program Dependencies

Things that should be installed so the program can run

* Tkinter
* Pynput
* Xterm 

To install them on linux you run these commands in the terminal 
* ```sudo apt-get install python3-tk```
* ```python3 -m pip install pynput```
* ```sudo apt-get install -y xterm```

Then just run the script by typing ``` python3  macroBuddy.py ```

How it Looks 
======

Heres the main windows when the program is ran

![Imgur](https://i.imgur.com/TMqy5if.png)

In the bottom right we have Record New Macro to record a script, currently its a prototype so there is no functionality to the button yet. Top right there is a open script button that allows to open previously recorded scripts and it allows the user to be able to edit the script or run it, this is what the user would see when they open the script. 

![Imgur](https://i.imgur.com/id1tqNj.png)


When we have the Text Editor open we can see that we have some menu options for the text editor in the top left, we also have a exit to terminal button in the lower right, it replaces the Record New Macro button whenever we are in the text editor. currently only the file menu is working, the edit menu will be implemented in the future below is a picture of what the menu looks like. 

![img](https://i.imgur.com/0XZD2Ue.png)

We have multiple options such as New, Open, Save, Save As, Run we can run the script from there as well, and we Exit which makes it so that we exit back to the terminal 
