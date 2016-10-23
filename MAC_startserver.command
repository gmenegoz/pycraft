#!/bin/bash
echo "Adventures In Minecraft"
echo "Canarymod Minecraft Server Version is 1.8"
echo "  Note - make sure Minecraft is using 1.8"
echo "By continuing you are indicating your agreement to our EULA https://account.mojang.com/documents/minecraft_eula)."
echo "Press any key to continue"
read -n 1 -s
cd "$( dirname "$0" )"
cd MyAdventures/stuff/server/
java -jar craftbukkit-1.10.2.jar
