from Tkinter import *
import os

click = 0

def left_down(event):
    global click
    os.system('cls')
    click += 1
    print('Clicks: ' + str(click))
    return True

def right_down(event):
    global click
    os.system('cls')
    click -= 1
    print('Clicks: ' + str(click))
    return True

def middle_down(event):
    global click
    os.system('cls')
    click = 0
    print('Clicks: ' + str(click))
    return True

root = Tk()

root.title('Click Here')

root.minsize(height=300, width=300)

root.bind("<Button-1>", left_down)
root.bind("<Button-3>", right_down)
root.bind("<Button-2>", middle_down)

root.mainloop()
