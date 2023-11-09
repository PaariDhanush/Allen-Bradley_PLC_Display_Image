
'''
the following import is only necessary because eip.py is not in this directory
'''
import sys
sys.path.append('..')

'''
Create a simple Tkinter window to display a
single variable.
Tkinter doesn't come preinstalled on all
Linux distributions, so you may need to install it.
Linux distributions, so you may need to install it.
For Ubuntu: sudo apt-get install python-tk
'''



from pylogix import PLC
from PIL import ImageTk, Image
from IPython.display import display, Image
from tkinter import Tk, Canvas
from tkinter import *
import PIL.Image
import tkinter.font as tkFont
import time


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

tagName1 = 'INPUT_1'
tagName2 = 'IMAGE_COUNT'
tagName3 = 'INPUT_3'
ipAddress = '192.168.1.13'

def main():
    '''
    Create our window and comm driver
    '''
    global root
    global comm
    global ProductionCount
    global ProductionCount1
    global ProductionCount2
    
    # create a comm driver
    comm = PLC()
    comm.IPAddress = ipAddress

    # create a tkinter window
    root = Tk()
    root.config(background='#EDF991')
    root.title = 'Production Count'
    root.geometry('1900x1700')
    
    # bind the "q" key to quit
    root.bind('q', lambda event:root.destroy())
    
    # create a labe to display our variable
    #ProductionCount = Label(root, text='n', fg='white', bg='black', font='Helvetica 100 bold')
    #ProductionCount.place(anchor=CENTER,relx=0.9, rely=0.3)
    
    ProductionCount1 = Label(root, text='n', fg='white', bg='red', font='Helvetica 100 bold')
    ProductionCount1.place(anchor=CENTER,relx=0.96, rely=0.1)
    
    #ProductionCount2 = Label(root, text='n', fg='white', bg='red', font='Helvetica 140 bold')
    #ProductionCount2.place(anchor=NE, relx=0.5, rely=0.9)

    

    root.after(1000, LogicTest)
    root.after(1000, UpdateValue)
    root.mainloop()
    comm.Close()
    
def ImageDis1():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/1.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()
def ImageDis2():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/2.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()
def ImageDis3():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/3.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()
def ImageDis4():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/4.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()
def ImageDis5():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/5.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()
def ImageDis6():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/6.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()
def ImageDis7():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/7.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()  
def ImageDis8():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/8.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()
    
def ImageDis9():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/9.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()
    
def ImageDis10():
    
    #topFrame =Frame(root,width=50,height=50)
    topFrame = Frame(root, width=100, height=100, bg='green')

    topFrame.grid(row=1,column=0,rowspan=2)

    #print("hello")

    #image=Image.open('/home/pi/Desktop/scene.jpg')    #comment out this

    image=PIL.Image.open('image/10.jpg')   #use this 

    photo = ImageTk.PhotoImage(image)

    #a.config(image=mi,compound=BOTTOM)

    a=Button(topFrame,image=photo,text="All stones preview",command=image,height=670,width=1270,font=tkFont.Font(weight="bold",size=15))

    a.grid(row=1, column=1)

    root.mainloop()      

def UpdateValue():
    '''
    Call ourself to update the screen
    '''
    #ProductionCount['text'] = comm.Read(tagName1).Value
    ProductionCount1['text'] = comm.Read(tagName2).Value
    #ProductionCount2['text'] = comm.Read(tagName3).Value
    #tagName1 = 'INPUT_1'
    #tagName2 = 'IMAGE_COUNT'
    #tagName3 = 'INPUT_3'
    root.after(500, LogicTest)
    root.after(500, UpdateValue)

        
def LogicTest():
    plc_Input = comm.Read(tagName2).Value
    for x in range(10):
        if x == 9: break
        if plc_Input == 0:
            ImageDis1()
        elif plc_Input == 1:
            ImageDis2()
        elif plc_Input == 2:
            ImageDis3()
        elif plc_Input == 3:
            ImageDis4()
        elif plc_Input == 4:
            ImageDis5()
        elif plc_Input == 5:
            ImageDis6()
        elif plc_Input == 6:
            ImageDis7()
        elif plc_Input == 7:
            ImageDis8()
        elif plc_Input == 8:
            ImageDis9()
        elif plc_Input == 9:
            ImageDis10()    
        else: 
            print("None")            
            #time.sleep(2)            
            #print("2Sec")


if __name__=='__main__':
    main()
