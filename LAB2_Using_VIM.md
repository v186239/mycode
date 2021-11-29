# Using Vim
Lab Objective
Throughout the course you'll find our documentation suggests using the vim text editor. Vim is an improved version of vi, so if you know vi you'll just be refreshing some basic skills in this lab.

Vim is the editor of choice for many developers and power users. It's a "modal" text editor based on the vi editor written by Bill Joy in the 1970s for a version of UNIX. It inherits the key bindings of vi but also adds a great deal of functionality that is missing from the original vi.

In most text editors the alphanumeric keys are only used to input those characters unless they're modified by a control key. In vim, the mode that the editor is in determines whether the alphanumeric keys will input those characters or move the cursor through the document. This is what is meant by 'modal.' When you first enter vim, you enter in the command mode.

Procedure
Review (read-only) the following vim commands:

To start editing changes by entering the INSERT mode:
press i
To stop editing and return to command mode:
press ESC
To save and quit:
press SHIFT + : press SHIFT and the PLUS keys at the same time
type wq (write out and quit)
press ENTER to confirm
To quit without saving:
press SHIFT + : press SHIFT and the PLUS keys at the same time
type q! (quit and ignore all changes)
press ENTER to confirm
Move into your home directory.

student@bchd:~$ cd

Now create a text file within the vim environment.

student@bchd:~$ vim secretofmi.test

Vim is entered in command mode. To write text, you'll need to change to INSERT mode. To begin writing text, press:

i
Notice in the bottom left corner of the screen it now says INSERT

Type a few sentences. Be sure to include some carriage returns, like the following:


Guybrush: Hi! I'm Guybrush Threepwood, and I'm a mighty pirate!
Pirate: Guybrush Threepwood? That's the most ridiculous name I've ever heard!
Guybrush: Oh yeah? What is yours?
Pirate: (matter-of-factly) My name is Mancomb Seepgood.
Okay, great! Now leave INSERT mode, and return to command mode, by pressing the escape key.

ESC
Notice that INSERT no longer is at the bottom left of the screen. Generally, pressing the escape key will always return you to the command mode.

Use the directional arrow keys on the keyboard to move the cursor around the screen.

Perform the following to save changes and return to the command line.

press SHIFT + : press SHIFT and then the COLON key at the same time
type wq (write out and quit)
press ENTER to confirm
Confirm that the file did correctly save by printing its contents. We can use the cat command to catenate, or read data from files, and print their contents to the screen.

student@bchd:~$ cat secretofmi.test

Edit the file secretofmi.test again.

student@bchd:~$ vim secretofmi.test

Remember, you enter vim in command mode. Take advantage of that and press the following capital letter to jump to the end of the file:

press SHIFT + g press SHIFT and the g keys at the same time
Press the following capital letter to begin appending at the end of the line (enter INSERT mode at the end).

press SHIFT + a press SHIFT and the a keys at the same time
You'll notice it says INSERT at the bottom left of your screen again. Once again you can type normally. Add some more text, such as the following:


Guybrush: Hi! I'm Guybrush Threepwood, and I'm a mighty pirate!
Pirate: Guybrush Threepwood? That's the most ridiculous name I've ever heard!
Guybrush: Oh yeah? What is yours?
Pirate: (matter-of-factly) My name is Mancomb Seepgood.
Taken from "The Secret of Monkey Island" by Lucas Arts (1990)
Okay, great! Now leave INSERT mode and return to command mode by pressing the escape key.

ESC
Perform the following to return to the command line without saving any changes.

press SHIFT + : press SHIFT and the COLON keys at the same time
type q! (quit without saving)
press ENTER to confirm
Confirm that none of the changes you just made were saved.

student@bchd:~$ cat secretofmi.test

Remove the file.

student@bchd:~$ rm secretofmi.test

Review a vim cheat sheet. These make very useful wall art, you may have seen one hanging in a colleague's workspace. http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html

If you want to get REALLY good at vim, run the following command. You don't need to do the entire tutorial now, but try reading the first few lessons.

student@bchd:~$ vimtutor

Quit with :wq

If you got stuck a few times, go back and try it again! Working within the vim environment is a basic Linux admin skill that is useful to everyone that expects to work at the Linux CLI.
