# pycraft
Modified, simplified and improved libraries to code in python via Minecraft

GETTING STARTED ITA: https://goo.gl/e1o5fD
GETTING STARTED ENGLISH (Work In Progress): https://goo.gl/XQ62tV

Based on the terrific idea and the original code of David Whale and Martin O'Hanlon (www.stuffaboutcode.com)

Alessandro Norfo, ale.norfo@gmail.com
Giuseppe Menegoz, gmenegoz@gmail.com

**RECIPES** at: https://goo.gl/bn1Uz2

# Getting Started
## Setup
As first thing, let’s install Python 2.7 on our computer!
At this link you will find an article in which we explain the details to install Python, and also some advice on the IDE (or the editor) you should use to write your own programs in Python:
https://apprendimentocreativo.wordpress.com/2016/10/ 11 / install-python / 
 
You will also need to install the Java Runtime Environment, to be able to launch the Spigot server. Then connect to the following address and download the appropriate installer for your operating system:
https://java.com/it/download/manual.jsp
 
After installing Python and Java, you can download Pycraft from this link:
https://github.com/gmenegoz/pycraft/archive/2.0.zip 
 
Now, extract the zip archive contents.
As you can see Pycraft works in a dedicated folder and you don’t need to install anything.
Opening the "pycraft" folder you will find yourself in front of a sub-folder "projects" and some other files.

"Projects" is the place where all your Python projects will reside. Inside that folder you will find a "stuff" sub-folder, you can safely ignore (but do not delete them! As it contains everything needed for Pycraft to work properly).
The 3 files ending in "_startserver" (one for each operating system) serve precisely to launch a Spigot server locally, on your computer, to which we would then connect to Minecraft so that our projects in Python can be run within the game. In order for a python script can communicate with a game of Minecraft, it is in fact your computer must be running the server.
But first we have to create a new profile to suit the Minecraft server that will be used by clicking on "NewProfile" and selecting "UseVersion: 1.10.2". For convenience we can call this profile "pycraft". Remember to select it each time you want to use pycraft.

Now we are ready to begin!
Let’s start the server by double-clicking the file that corresponds to your operating system.
Once you launched Minecraft, choose "multiplayer" then "direct connect", typing "localhost" as address.
If you access the world of Minecraft it means that everything worked properly :) ...otherwise try to re-read the instructions above :(
