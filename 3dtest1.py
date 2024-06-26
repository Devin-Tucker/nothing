import ursina
from ursina import *
from fpc import FirstPersonController
import time

app = Ursina()

for z in range(10):
    for x in range(10):
        cube = Entity(model='cube', color=color.gray, position = (x, 0, z), parent=scene, origin_y=0.5, texture='white_cube')
        cube.collider = BoxCollider(cube, center=Vec3(0,0.5,0), size=Vec3(1,1,1))

player = FirstPersonController()
player.gravity = 0.8
player.mouse_sensitivity = Vec3(80 ,80 ,80)
player.cursor.enabled = False

gun = Entity(model='cube', color=color.gold, position=(1, 3, 1), parent=player, scale=(0.1, 0.1, 1))
gun_model = load_model('path_to_your_gun_model')
gun.scale = (0.5, 0.2, 1)

class Bullet(Entity):
    def __init__(self, direction, speed, lifetime=4):
        super().__init__(model='sphere', color=color.rgb(120, 0, 30), position=gun.world_position, scale = 0.1)
        self.collider = SphereCollider(self, center=Vec3(0,0,0), radius=0.1)
        
        self.velocity = direction * speed * 2
        self.lifetime = lifetime

    def update(self):
        self.position += self.velocity * time.dt
        self.lifetime -= time.dt
        self.velocity.y -= time.dt * 2

target = Entity(model='sphere', color=color.red, scale=1, position = (30, 10, 10))
target_collider = SphereCollider(target, center=Vec3(0,0,0), radius=1)

bullet = None

def input(key):
    global bullet
    if key == 'left mouse down':
        bullet = Bullet(direction=gun.forward, speed=20)

def update():
    global bullet
    gun.rotation = player.camera_pivot.rotation
    gun.y = 1.5 + (player.camera_pivot.rotation_y + -1.5 * math.sin(math.radians(player.camera_pivot.rotation_x)))
    
    if held_keys['r']:
        player.y = 20

    if bullet and bullet.intersects(target): 
        target.color = color.green
        invoke(destroy, target, delay = 2)



app.run()