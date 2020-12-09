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
* ```sudo apt install python3-pip```
* ```pip3 install pynput```
* ```sudo apt-get install -y xterm```

Then just run the script by typing ``` python3  macroBuddy.py ```

How it Looks 
======

Heres the main windows when the program is ran


![img](https://i.imgur.com/Zzs5DTM.png)



In the bottom right we have Record New Macro to record a script or we can hit one of the menu options on the top, if the bottom button is pressed it will toggle to stop recording and an xterm terminal will appear where the user can start inputtin the commands that they want to be converted into a shell script. Below is a picture of what the xterm terminal looks like within the application. 

![img](https://i.imgur.com/oJBKxlJ.png)


Once stop recording is pressed it will kill the terminal and it will ask where the user wants to save their shell script. Top right there is a open script button that allows the user to open scripts that were just saved or were saved in the past and it allows the user to be able to edit the script if any mistakes were made while recording their macro, once its open the user can run the script and it will run the commands from the home PATH of the user, and it will execute those commands in the shell that the user used to run the python script, this is what the user would see when they click on the open script button and select a file. 

![img](https://i.imgur.com/WLP6iTy.png)


When we have the Text Editor open we can see that we have some menu options for the text editor in the top left, we also have a exit to terminal button in the lower right, it replaces the Record New Macro button whenever we are in the text editor. The file menu is working and so is the the edit menu below is a picture of what the menu looks like. 

![img](https://i.imgur.com/ps2i7oL.png)

We have multiple options such as New, Open, Save, Save As, and we have Run we can run the script from there as well, and we have Exit which makes it so that we exit back to the terminal 
