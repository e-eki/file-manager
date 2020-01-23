from tkinter import *
from blocks.currentDirectory import CurrentDirectory

# размеры и положение главного окна приложения
height = 390
width = 400
xCoordinate = 450
yCoordinate = 180
 
root = Tk()
root.title("Python File Manager")
root.geometry("{}x{}+{}+{}".format(width, height, xCoordinate, yCoordinate))


currentDir = CurrentDirectory(root)
currentDir.display()

root.mainloop()
