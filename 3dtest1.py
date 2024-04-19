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
    camera.y += held_keys['e'] * time.dt
    camera.y -= held_keys['q'] * time.dt
    camera.x += held_keys['d'] * time.dt
    camera.x -= held_keys['a'] * time.dt
    camera.z += held_keys['w'] * time.dt
    camera.z -= held_keys['s'] * time.dt

def update():
    camera.rotation_y += held_keys['right arrow'] * 1
    camera.rotation_y -= held_keys['left arrow'] * 1
    camera.rotation_x += held_keys['up arrow'] * 1
    camera.rotation_x -= held_keys['down arrow'] * 1

app.run()