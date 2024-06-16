from tkinter import *
from tkinter.ttk import *
from turtle import *
from turtlefigures import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import random
from PIL import ImageTk, Image


#make the window
root=Tk()
root.title("Fractal Assignment")
screenWidth=root.winfo_screenwidth()
screenHeight=root.winfo_screenheight()
root.geometry("%dx%d" % (screenWidth, screenHeight))
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


style = Style()
style.theme_use('clam')



#make the interface


horizontalpw = PanedWindow(orient=HORIZONTAL)
verticalpw = PanedWindow(orient=VERTICAL)
horizontalpw.grid(row=0, column=0, sticky ="nsew")
verticalpw.grid(row=0, column=1, sticky ="nsew")


#make the control panel
controlFrame=LabelFrame(root, text="Control Panel")
controlFrame.grid(row=0,column=0,columnspan=6)
horizontalpw.add(controlFrame)




notebook=Notebook(controlFrame)
notebook.grid(row=1, column=0)


shapeControlFrame=Frame(controlFrame)
shapeControlFrame.grid(row=0,column=0,columnspan=6)

shapeLabel=Label(shapeControlFrame,text="Shape")
shapeLabel.grid(row=1, column=0,padx=(5,5),pady=(10, 10))
comboBox = Combobox(shapeControlFrame,state='readonly')
comboBox.grid(row=1,column=1,columnspan=4,sticky="ew",padx=(5,10),pady=(10, 10))
def shapeChange(evt):
    descriptionText.configure(state="normal")
    descriptionText.delete("0.0", END)
    descriptionText.insert("0.0",fractal_list[comboBox.current()].description)
    descriptionText.configure(state="disabled")
    newImg=Image.open(f"images/{comboBox.current()}.png")
    newImg = newImg.resize((400, 350))
    newImg = ImageTk.PhotoImage(newImg)
    imgLabel.configure(image=newImg)
    imgLabel.image=newImg
    
    
comboBox.bind('<<ComboboxSelected>>', shapeChange)
figureList=[]
for i in range(len(fractal_list)):
    
    figureList.append(fractal_list[i].name)
    
comboBox['values'] = figureList
comboBox.current(0)



orderLabel=Label(shapeControlFrame,text="Order")
orderLabel.grid(row=2, column=0,padx=(5,5),pady=(0, 10))

notebook.add(shapeControlFrame,text="Fractals")
orderVal=DoubleVar()
orderVal.set(1)
def orderSliderChange(value):
    
    orderVal.set('%d' % float(value))
 
  
orderSlider= Scale(
    shapeControlFrame,
    from_=1,
    to=25,
    orient='horizontal',
   command=orderSliderChange,
    variable=orderVal
)

orderSlider.grid(row=2,column=1,columnspan=3,sticky="ew",padx=(5,5),pady=(0, 10))
orderSliderVal=Label(shapeControlFrame,textvariable=orderVal,width=2)
orderSliderVal.grid(row=2, column=4,padx=(0,5),pady=(0, 10))

lengthLabel=Label(shapeControlFrame,text="Length")
lengthLabel.grid(row=3, column=0,padx=(5,5),pady=(0, 10))

lengthStr=StringVar()
lengthEntry=Entry(shapeControlFrame, textvariable=lengthStr)
lengthEntry.grid(row=3,column=1, columnspan=4,sticky="ew",padx=(5,10),pady=(0, 10))

separator1 = Separator(shapeControlFrame, orient='horizontal')
separator1.grid(row=4,column=0,columnspan=5, sticky='ew')
t=TerminateFunc(False)
#Buttons
def clearF():
    #Clear the entries
    orderVal.set(1)
    lengthStr.set("")
    msg=messagebox.askquestion("Clear Sketch", "Are you sure you want to clear the sketch?", icon='warning')
    if msg=="yes":
        pen.home()
        pen.clear()
        while(pen.position()!=(0,0)):
           pen.clear()
        
        startYPos.set("middle")
        


def drawF():
    
    if(t.isRunning==False):
        if(lengthEntry.get()==""):
            messagebox.showerror(title="Error",message="Error: Length Cannot be Empty")
        elif (not lengthEntry.get().isnumeric()):
             messagebox.showerror(title="Error",message="Error: Length must be a whole number")
        elif (int(lengthEntry.get())<2):
            messagebox.showerror(title="Error",message="Error: Length cannot be less than 2")
                                        
        else:
            order=int(orderVal.get())
            length=int(lengthEntry.get())
            pen.down()
           
            
            #Call a turtle Method
            figureIndex = comboBox.current()
            t.isRunning=True
            drawButton.config(text="Stop")
            drawShape(pen,figureIndex,order,length,t)
            t.isRunning=False 
            drawButton.config(text="Draw")
           
           
            
        
    else:
          pen.up()
          t.isRunning=False
          messagebox.showinfo(title="Please Wait!", message="Please wait for a few seconds for the fractal drawing to stop")
          drawButton.config(text="Draw")
          
          

            
    

def saveF():
    try:
      canvas.postscript(file="canvas_drawing.ps", colormode='color')
    except:
      messagebox.showerror(title="Error",message="Error: Oops something went wrong")
    else:
      messagebox.showinfo(title="Success", message="Image saved successfully")
    
    
   
    
clearButton=Button(shapeControlFrame,text="Clear",command=clearF)
clearButton.grid(row=5,column=0,padx=(5,5),pady=(25,25))

drawButton=Button(shapeControlFrame,text="Draw",command=drawF)
drawButton.grid(row=5, column=2,padx=(10,0),pady=(25,25))

saveButton=Button(shapeControlFrame,text="Save Vector",command=saveF)
saveButton.grid(row=5, column=3,padx=(10,0),pady=(25,25))

separator2 = Separator(shapeControlFrame, orient='horizontal')
separator2.grid(row=6,column=0,columnspan=5, sticky='ew')

img=Image.open(f"images/{comboBox.current()}.png")
img = img.resize((400, 350))
img = ImageTk.PhotoImage(img)

# Create a Label Widget to display the text or Image
imgLabel = Label(shapeControlFrame, image = img)
imgLabel.grid(row=7, column=0,columnspan=5,padx=(10,0),pady=(25,0),sticky="nsew")

#Pen section



penControlFrame=Frame(controlFrame)
penControlFrame.grid(row=0,column=0,columnspan=5)
penSizeLabel=Label(penControlFrame,text="Pen Size")
penSizeLabel.grid(row=1, column=0,padx=(5,5),pady=(10, 10))
def penSizeSliderChange(value):
    
    penSizeVal.set('%d' % float(value))
    pen.width(int(penSizeVal.get()))
 
penSizeVal=DoubleVar()
penSizeVal.set(3)
penSizeSlider= Scale(
    penControlFrame,
    from_=1,
    to=20,
    orient='horizontal',
   command=penSizeSliderChange,
    variable=penSizeVal
)

penSizeSlider.grid(row=1,column=1,columnspan=4,sticky="ew",padx=(5,5),pady=(10, 10))
penSizeSliderVal=Label(penControlFrame,textvariable=penSizeVal,width=2)
penSizeSliderVal.grid(row=1, column=5,padx=(0,5),pady=(0, 10))



penShapeLabel=Label(penControlFrame,text="Pen Shape")
penShapeLabel.grid(row=2, column=0,padx=(5,5),pady=(0, 10))

penShapeOption=StringVar()
def setPenShape(value):
    pen.shape(value)
penShapes=["arrow", "turtle", "circle", "square", "triangle", "classic"]
penShapeMenu=OptionMenu(penControlFrame,penShapeOption,penShapes[5],*penShapes,command=setPenShape)
penShapeMenu.grid(row=2, column=1,columnspan=4, sticky='ew',padx=(5,5),pady=(0, 10))

penColorLabel=Label(penControlFrame,text="Pen Color")
penColorLabel.grid(row=3, column=0,padx=(5,5),pady=(0, 10))
def setPenColor():
    msg=messagebox.askyesno(title="Pick a color",message="Do you want to use a random color?")
  
    if (msg):
          pen.fillcolor(random.random(),random.random(),random.random())

    else:
          colors = askcolor(title="Tkinter Color Chooser")
    
          if(colors[1]):
        
              pen.fillcolor(colors[1])
        
  


penColorBtn=Button(
    penControlFrame,
    text='Select a Color',
    command=setPenColor);
penColorBtn.grid(row=3,column=1,columnspan=4, sticky='ew',padx=(5,5),pady=(0, 10))

def setPenStrokeColor():
    msg=messagebox.askyesno(title="Pick a color",message="Do you want to use a random color?")
    if (msg):
           pen.color(random.random(),random.random(),random.random())

    else:
           colors = askcolor(title="Tkinter Color Chooser")
           if(colors[1]):
              pen.color(colors[1])

penStrokeColorLabel=Label(penControlFrame,text="Stroke Color")
penStrokeColorBtn=Button(
    penControlFrame,
    text='Select a Color',
    command=setPenStrokeColor);
penStrokeColorBtn.grid(row=4,column=1,columnspan=4, sticky='ew',padx=(5,5),pady=(0, 10))
penStrokeColorLabel.grid(row=4, column=0,padx=(5,5),pady=(0, 10))

def setBgColor():
    msg=messagebox.askyesno(title="Pick a color",message="Do you want to use a random color?")
    if (msg):
           screen.bgcolor(random.random(),random.random(),random.random())

    else:
        colors = askcolor(title="Tkinter Color Chooser")
        if(colors[1]):
            screen.bgcolor(colors[1])


bgColorLabel=Label(penControlFrame,text="Bg Color")
bgColorLabel.grid(row=5, column=0,padx=(5,5),pady=(0, 10))
bgColorBtn=Button(
    penControlFrame,
    text='Select a Color',
    command=setBgColor);
bgColorBtn.grid(row=5,column=1,columnspan=4, sticky='ew',padx=(5,5),pady=(0, 10))

penSpeedLabel=Label(penControlFrame,text="Pen Speed")
penSpeedLabel.grid(row=6, column=0,padx=(5,5),pady=(0, 10))

penSpeedOption=StringVar()
def setPenSpeed(value):
    pen.speed(value)
penSpeeds=["fastest","fast" ,"normal" ,"slow"   ,"slowest",]
penSpeedMenu=OptionMenu(penControlFrame,penSpeedOption,penSpeeds[0],*penSpeeds,command=setPenSpeed)
penSpeedMenu.grid(row=6, column=1,columnspan=4, sticky='ew',padx=(5,5),pady=(0, 10))


startPos = StringVar()
startPos.set("Center")

def setStartPos():
    w=int(canvas["width"])
    h=int(canvas["height"])
    selected_option = startPos.get()
    match selected_option:
        case "Dead Left":
            
             pen.up();
             pen.home();

             pen.backward(w/2);pen.down()
        case "Left":
             pen.up();pen.home();pen.backward(w/4);pen.down()
        case "Center":
             pen.up();pen.goto(0,0);pen.down();
        case "Right":
             pen.up();pen.home();pen.forward(w/2);pen.down()
        case "Dead Right":
             pen.up();pen.home();pen.forward(w/1.45);pen.down()
             
startPosLabel=Label(penControlFrame,text="Start X Position")
startPosLabel.grid(row=7, column=0,padx=(5,5),pady=(0, 10))

radio_button_1 = Radiobutton(penControlFrame, text="Dead Left", variable=startPos, value="Dead Left",
                                command=setStartPos)
radio_button_1.grid(row=8, column=0, sticky='ew',padx=(2,2),pady=(0, 10))
radio_button_2 = Radiobutton(penControlFrame, text="Left", variable=startPos, value="Left",
                                command=setStartPos)
radio_button_2.grid(row=8, column=1, sticky='ew',padx=(2,2),pady=(0, 10))
radio_button_3 = Radiobutton(penControlFrame, text="Center", variable=startPos, value="Center",
                                command=setStartPos)
radio_button_3.grid(row=8, column=2, sticky='ew',padx=(2,2),pady=(0, 10))
radio_button_4 = Radiobutton(penControlFrame, text="Right", variable=startPos, value="Right",
                                command=setStartPos)
radio_button_4.grid(row=8, column=3, sticky='ew',padx=(2,2),pady=(0, 10))
radio_button_5 = Radiobutton(penControlFrame, text="Dead Right", variable=startPos, value="Dead Right",
                                command=setStartPos)
radio_button_5.grid(row=8, column=4, sticky='ew',padx=(2,2),pady=(0, 10))


startYPos = StringVar()
startYPos.set("middle")
def setStartYPos():
    w=int(canvas["width"])
    h=int(canvas["height"])
    selected_option = startYPos.get()
    match selected_option:
        case "top":
            
             pen.up();
             pen.goto(pen.xcor(),h/2)
             pen.down()
        case "middle":
             pen.up();pen.goto(pen.xcor(),0);pen.down()
        case "bottom":
             pen.up();pen.goto(pen.xcor(),-h/2);pen.down();
        
             
startYPosLabel=Label(penControlFrame,text="Start Y Position")
startYPosLabel.grid(row=9, column=0,padx=(5,5),pady=(0, 10))

radio_btn_1 = Radiobutton(penControlFrame, text="Topmost", variable=startYPos, value="top",
                                command=setStartYPos)
radio_btn_1.grid(row=10, column=0, sticky='ew',padx=(2,0),pady=(0, 10))
radio_btn_2 = Radiobutton(penControlFrame, text="Middle", variable=startYPos, value="middle",
                                command=setStartYPos)
radio_btn_2.grid(row=10, column=1, sticky='ew',padx=(2,2),pady=(0, 10))
radio_btn_3 = Radiobutton(penControlFrame, text="Bottom", variable=startYPos, value="bottom",
                                command=setStartYPos)
radio_btn_3.grid(row=10, column=2, sticky='ew',padx=(2,2),pady=(0, 10))


hideTurtle = IntVar()

def toggleTurtle():
    if (hideTurtle.get() == 1):
        pen.hideturtle()
    else:
        pen.showturtle()
        

c1 = Checkbutton(penControlFrame, text='Hide Turtle',variable=hideTurtle, onvalue=1, offvalue=0, command=toggleTurtle)
c1.grid(row=11, column=0, sticky='ew',padx=(2,2),pady=(0, 10))


notebook.add(penControlFrame,text="Config")

#####CANVAS########

canvasFrame=LabelFrame(root,text="Canvas")
canvas=Canvas(canvasFrame,width=800,height=screenHeight-300)
canvasFrame.grid(row=1,column=1,sticky="ew")
canvas.pack(fill=BOTH, expand=TRUE)

horizontalpw.add(verticalpw)

verticalpw.add(canvasFrame)

# make a screen and setup the bg
screen = TurtleScreen(canvas)


screen.bgcolor("black")

# make a turtle pen connected with the screen
pen = RawPen(screen)
pen.color("gold")
pen.speed(0)
pen.width(int(penSizeVal.get()))




#Description

descriptionFrame=LabelFrame(root, text="Description")
descriptionFrame.grid(row=1,column=3,sticky="ew",rowspan=3)

descriptionText= ScrolledText(descriptionFrame,font = ("Times New Roman",16))
descriptionText.insert(END,fractal_list[comboBox.current()].description)
descriptionText.pack(side="left",fill=BOTH,expand=TRUE)

descriptionText.configure(state ='disabled')

verticalpw.add(descriptionFrame)
#loop it
root.mainloop()
