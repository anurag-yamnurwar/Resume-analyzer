# Rock-Paper-Scissors-Game
#import library
from tkinter import *
import random
#initialize window
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg ='white')
#heading
Label(root, text = 'Rock-Paper-Scissors' , font='arial 20 bold', bg = 'white').pack()
##user choice
user_take = StringVar()
Label(root, text = 'Choose any one: Rock, Paper, Scissors' , font='arial 15 bold', bg = 'white').place(x = 10,y=60)
Entry(root, font = 'arial 15', textvariable = user_take , bg = 'white').place(x=90 , y = 130)
#computer choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick ==2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
## function to play
Result = StringVar()
def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you loose,computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you loose,computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win ,computer select paper')
    else:
        Result.set('Invalid: choose any one -- rock, paper, scissors')
##fun to reset
def Reset():
    Result.set("") 
    user_take.set("")
## fun to exit
def Exit():
    root.destroy()
# buttons
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='white',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='yellow' ,command = play).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='red' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='grey' ,command = Exit).place(x=230,y=310)
root.mainloop()
