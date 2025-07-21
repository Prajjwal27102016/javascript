from ursina import *

app = Ursina()

# Make sure the texture path is correct or use a built-in texture for testing
background = Entity(model='quad', texture='geometery dash.JPEG', scale=55, z=-10, y=0)

camera.orthographic = True
camera.fov = 10

app.run()