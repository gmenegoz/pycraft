from pycraft import *

# Store player position in a variable
pos = where()
# Write on chat that position (just as a test)
chat(pos)

# Forever
while True:

    # Sequentially create many spheres with different materials
    # but in the same absolute position
    sphere(grass, 20, x=pos.x+25, y=pos.y, z=pos.z, absolute=True)
    sphere(gold, 20, x=pos.x+25, y=pos.y, z=pos.z, absolute=True)
    sphere(ice, 20, x=pos.x+25, y=pos.y, z=pos.z, absolute=True)