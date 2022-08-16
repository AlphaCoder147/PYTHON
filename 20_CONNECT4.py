import numpy as np
import pygame
import math
import tkinter as tk
from tkinter import messagebox
import winsound
ROW=6
COLUMN=7

def createBoard():
    board=np.zeros((ROW,COLUMN))
    return board

def piece_drop(board,row,col,piece):
    board[row][col]=piece

def location_valid(board,col):
    return board[ROW -1][col]==0

def Getnext_open_row(board,col):
    for row in range (ROW):
        if board[row][col]==0:
            return row

def board_print(board):
    print(np.flip(board,0))   


def win_move(board,piece):
    for c in range(COLUMN-3):
        for r in range(ROW):
            if board[r][c]==piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece:
                return True 
    for c in range(COLUMN):
        for r in range(ROW-3):
            if board[r][c]==piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece:
                return True
    for c in range(COLUMN-3):
        for r in range(ROW-3):
            if board[r][c]==piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece:
                return True
    for c in range(COLUMN-3):
        for r in range(3,ROW):
            if board[r][c]==piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece:
                return True        
def Drawboard(board):
    for c in range(COLUMN):
        for r in range(ROW):
            pygame.draw.rect(Screen,(0,0,255),(c*SQRSIZE,r*SQRSIZE+SQRSIZE,SQRSIZE,SQRSIZE))
            pygame.draw.circle(Screen,(0,0,0),(int(c*SQRSIZE+SQRSIZE/2),int(r*SQRSIZE+SQRSIZE+SQRSIZE/2)),int(SQRSIZE/2-5))
    for c in range(COLUMN):
        for r in range(ROW):
            if board[r][c]==1:
                pygame.draw.circle(Screen,(255,0,0),(int(c*SQRSIZE+SQRSIZE/2),height-int(r*SQRSIZE+SQRSIZE/2)),int(SQRSIZE/2-5))
            elif board[r][c]==2:
                pygame.draw.circle(Screen,(255,255,0),(int(c*SQRSIZE+SQRSIZE/2),height-int(r*SQRSIZE+SQRSIZE/2)),int(SQRSIZE/2-5))            
    pygame.display.update()
def msg_box(subject,content):
    root=tk.Tk()
    root.attributes("-topmost",True)
    root.withdraw()
    messagebox.showinfo(subject,content)
    try:
        root.destroy()
    except:
        pass   
board=createBoard()

gameOver=False 

turn=0

pygame.init()

SQRSIZE=100
width=COLUMN*SQRSIZE
height=(ROW+1)*SQRSIZE
size=(width,height)
Screen=pygame.display.set_mode(size)
pygame.display.set_caption("Connect 4")
Drawboard(board)
pygame.display.update()

while not gameOver:
    events=pygame.event.get()
    for event in events:
        if(event.type==pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type==pygame.MOUSEMOTION):
            pygame.draw.rect(Screen,(0,0,0),(0,0,width,SQRSIZE))
            posx=event.pos[0]
            if turn==0:
                pygame.draw.circle(Screen,(255,0,0),(posx,int(SQRSIZE/2)),int(SQRSIZE/2-5))
            else:
                pygame.draw.circle(Screen,(255,255,0),(posx,int(SQRSIZE/2)),int(SQRSIZE/2-5))  
            pygame.display.update()                    
        if(event.type==pygame.MOUSEBUTTONDOWN):
            if turn==0:
                posx=event.pos[0]
                col=int(math.floor(posx/SQRSIZE))
                if location_valid(board,col):
                    row=Getnext_open_row(board,col)
                    piece_drop(board,row,col,1)
                    winsound.PlaySound("game_sound1.wav",winsound.SND_ASYNC)
                    if win_move(board,1):
               # board_print(board)
                        winsound.PlaySound("GameOver_sound1.wav",winsound.SND_ASYNC)
                        msg_box("GAME OVER!!","PLAYER 1 WINS!!")
                        gameOver=True    
            else:
                posx=event.pos[0]
                col=int(math.floor(posx/SQRSIZE))
                if location_valid(board,col):
                    row=Getnext_open_row(board,col)
                    piece_drop(board,row,col,2)
                    winsound.PlaySound("game_sound1.wav",winsound.SND_ASYNC)
                    if win_move(board,2):
                        winsound.PlaySound("GameOver_sound1.wav",winsound.SND_ASYNC)
                        msg_box("GAME OVER!!","PLAYER 2 WINS!!")
                        gameOver=True
            Drawboard(board)
            pygame.display.update()            
            turn+=1
            turn=turn%2        
