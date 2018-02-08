import os
import urllib
import subprocess
import sys

#print('By continuing you are indicating your agreement to our EULA https://account.mojang.com/documents/minecraft_eula')
#raw_input('Press ENTER to continue...')

# Launch spigot server

nplatform = sys.platform == "win32"

if mswinplatform:
    subprocess.Popen(['java', '-jar', 'spigot-1.10.2.jar'], creationflags=subprocess.CREATE_NEW_CONSOLE, cwd='server/')
else:
    subprocess.Popen(" ".join(['java', '-jar', 'spigot-1.10.2.jar']), shell=True, cwd='server/')
    


subprocess.Popen(['python', 'scratch_pycraft.py'], cwd='projects/pycraft/')

# Check for scratch_pycraft file
#os.chdir('projects/pycraft/')
#filenames = os.listdir('.')
#check = False
#for f in filenames:
    #if f == 'scatch_pycraft.py':
        #check = True
        #print('scratch_pycraft.py found, executing it...')
        #subprocess.Popen(['python', 'scratch_pycraft.py'], shell=True)
#if not check:
    #try:
        #urllib.urlretrieve('https://raw.githubusercontent.com/sprintingkiwi/pycraft_mod/development/scratch_pycraft.py',
                           #'scratch_pycraft.py')
    #except:
        #print('Cannot retrieve scratch_pycraft.py')
    #else:
        #print('scratch_pycraft.py successfully retrieved, executing it...')
        #subprocess.Popen(['python', 'scratch_pycraft.py'], shell=True)

