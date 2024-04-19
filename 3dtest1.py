import ursina
from ursina import *


app = ursina.Ursina()
app = Ursina()

list()
for i in range(5):
        cube = Entity(model='cube', color=color.red, scale=(1, 1, 1))
        cube.x = i * 2

list()
for i in range(10):
        sphere = Entity(model = 'sphere', color=color.green, scale=(2, 2, 2))
        sphere.y = i * 4

# Create a camera
camera = EditorCamera()

def update():
    # Move the camera
    camera.y += held_keys['w'] * time.dt
    camera.y -= held_keys['s'] * time.dt
    camera.x += held_keys['d'] * time.dt
    camera.x -= held_keys['a'] * time.dt

app.run()