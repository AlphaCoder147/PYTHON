from ursina import *
import random
def rotate():
    num=random.randint(0,1)
    if num==0:
        dice.rotation_x+=90
    elif num==1:    
        dice.rotation_y+=90
   
    
app=Ursina()
dice=Entity(model="Dice_Obj.obj",texture="assets\Dice_Base_Color.png",scale=5)
button=Button(text="Click Me!!",position=(0,-0.4),scale=0.15)
button.on_click=rotate

app.run()