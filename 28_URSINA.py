from ursina import *
app=Ursina()
cube=Entity(model="Dice_Obj.obj",scale=3,texture="assets\Dice_Base_Color.png")

def update():
    cube.rotation_x+=0.5*time.dt*100
    cube.rotation_y+=0.5*time.dt*100
app.run()    