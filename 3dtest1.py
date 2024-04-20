import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

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


player = FirstPersonController()
player.gravity = 0
player.mouse_sensitivity = Vec3(80 ,80 ,80)

app.run()