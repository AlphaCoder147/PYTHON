#IMPORTS
import pygame
import random
import tkinter as tk
from tkinter import messagebox
import time
import winsound
#Initialisation of display
pygame.init()
width,height=600,600
gameScreen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
#Initialisation of objects
x,y=300,300
dx,dy=10,0
foodX,foodY=random.randrange(0,width)//10*10,random.randrange(0,height)//10*10
list_body=[(x,y)]
clock=pygame.time.Clock()
GameOver=False
#Defining required functions
def Snake():
    global x,y,foodX,foodY,GameOver,score 
    x= (x+dx)%width         #movement up and down
    y= (y+dy)%height        #movement right and left
    #Game Over condition
    if ((x,y) in list_body):
         GameOver=True
         return
    #Regenerating Food after being eaten and Increasing Snake Size 
    list_body.append((x,y))
    score=0
    if (foodX==x and foodY==y):
        winsound.PlaySound("Eating Apple.wav",winsound.SND_ASYNC)
        score+=1
        while((foodX,foodY) in list_body):
            foodX,foodY=random.randrange(0,width)//10*10,random.randrange(0,height)//10*10
    else:
        del list_body[0]
    #Displaying Food    
    gameScreen.fill((0,0,0))
    pygame.draw.rect(gameScreen,(0,255,0),[foodX,foodY,10,10])
    for (i,j) in list_body:
        pygame.draw.rect(gameScreen,(255,0,0),[i,j,10,10])
    pygame.display.update()
# Message Bx    
def msg_box(subject,content):
    root=tk.Tk()
    root.attributes("-topmost",True)
    root.withdraw()
    messagebox.showinfo(subject,content)
    try:
        root.destroy()
    except:
        pass        
#MAIN GAME LOOP    
while True:
    #Game Over Condition in Game
    if (GameOver):
        winsound.PlaySound("GameOver_sound1.wav",winsound.SND_ASYNC)
        msg_box("You Lost!!","Play Again...")
        pygame.quit()
#Creating Events such as movement and quiting 
    events=pygame.event.get()
    for event in events:
        if(event.type==pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type==pygame.KEYDOWN):     #KEYPRESS
            if(event.key==pygame.K_a):      #LEFT
                if(dx!= 10):
                   dx= -10
                dy=0
            elif(event.key==pygame.K_d):    #RIGHT
                if(dx!= -10):
                    dx= 10
                dy=0
            elif(event.key==pygame.K_w):    #UP
                dx=0
                if(dy!= 10):
                    dy= -10
            elif(event.key==pygame.K_s):    #DOWN
                dx= 0
                if(dy!= -10):
                    dy= 10
            else:
                continue
            Snake()
    if(not events):                         #SNAKE displayed even when there is no key press
        Snake()
    
    clock.tick(17)                          #FPS
                                
    


