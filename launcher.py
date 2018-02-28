import subprocess

print("Start")

# Launch spigot server
p = subprocess.Popen(['java', '-jar', 'spigot-1.12.2.jar'], cwd='server/')
