
from ursina import *
from ursina.prefabs.first_person_controller \
  import FirstPersonController

app = Ursina()

player = FirstPersonController()
ground = Entity(
  model='plane',
  texture='grass',
  collider='mesh',
  scale=(100,1,100)
)
for i in range(4):
  for j in range(4):
    robot = FrameAnimation3d(
      'assets\\robot',
      position=(4*i,0,4*j),
      fps=18,
      scale=0.015,
      color=color.black66
    )

Sky()

app.run()