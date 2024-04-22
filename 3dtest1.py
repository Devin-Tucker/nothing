import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = ursina.Ursina()
app = Ursina()

for z in range(10):
    for x in range(10):
        cube = Entity(model='cube', color=color.gray, position = (x, 0, z), parent=scene, origin_y=0.5, texture='grass')
        cube.collider = BoxCollider(cube, center=Vec3(0,0.5,0), size=Vec3(1,1,1))

for z in range(10):
    for x in range(10):
        for i in range(1):
            cube = Entity(model='cube', color=color.gray, position=(x+10+x, x, z), parent=scene, origin_y=1, texture='grass', collider='box')
            cube.collider = BoxCollider(cube, center=Vec3(0,0.5,0), size=Vec3(1,1,1))

for z in range(10):
    for x in range(10):
        for i in range(1):
            cube = Entity(model='cube', color=color.gray, position=(z, x, x+10+x), parent=scene, origin_y=1, texture='grass', collider='box')
            cube.collider = BoxCollider(cube, center=Vec3(0,0.5,0), size=Vec3(1,1,1))

for z in range(10):
    for x in range(10):
        sphere = Entity(model='sphere', color=color.blue, position=(25, x, x), parent=scene, orgin_y=4)
        sphere.collider = SphereCollider(sphere, center=Vec3(0,0.5,0), radius=0.5)
player = FirstPersonController()
player.gravity = 0.5
player.mouse_sensitivity = Vec3(80 ,80 ,80)

def update():
    if held_keys['r']:
        player.y = 20

app.run()