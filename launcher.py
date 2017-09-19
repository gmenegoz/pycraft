import os
import urllib
import subprocess
from subprocess import CREATE_NEW_CONSOLE

#print('By continuing you are indicating your agreement to our EULA https://account.mojang.com/documents/minecraft_eula')
#raw_input('Press ENTER to continue...')


# Launch spigot server
#os.chdir('server/')
#os.system('java -jar spigot-1.10.2.jar')
subprocess.Popen(['java', '-jar', 'spigot-1.10.2.jar'], creationflags=CREATE_NEW_CONSOLE, cwd='stuff/server/')


# Check for scratch_pycraft file
os.chdir('stuff/')
filenames = os.listdir('.')
check = False
for f in filenames:
    if f == 'scatch_pycraft.py':
        check = True
        print('scratch_pycraft.py found, executing it...')
        subprocess.Popen(['python', 'scratch_pycraft.py'], shell=True)
if not check:
    try:
        urllib.urlretrieve('https://raw.githubusercontent.com/sprintingkiwi/pycraft_mod/development/scratch_pycraft.py',
                           'scratch_pycraft.py')
    except:
        print('Cannot retrieve scratch_pycraft.py')
    else:
        print('scratch_pycraft.py successfully retrieved, executing it...')
        subprocess.Popen(['python', 'scratch_pycraft.py'], shell=True)

