import ursina
from ursina import *


app = ursina.Ursina()
app = Ursina()

# Create a cube
cube = Entity(model='cube', color=color.red, scale=(1, 1, 1))

# Create a sphere
sphere = Entity(model='sphere', color=color.blue, scale=(1, 1, 1))

# Create a camera
camera = EditorCamera()

def update():
    # Move the camera
    camera.y += held_keys['w'] * time.dt
    camera.y -= held_keys['s'] * time.dt
    camera.x += held_keys['d'] * time.dt
    camera.x -= held_keys['a'] * time.dt

app.run()