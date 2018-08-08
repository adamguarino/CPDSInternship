#tkinter is a basic GUI application for Python. This is a minimal barebones class to take a bit of text as input and return it
from tkinter import *

class Gui:
    def __init__(self):
        self.wd = Tk()  #initializes the window
        self.wd.title("databaseGUI")    #gives the window a name
        self.wd.geometry("500x200")     #sets window size
        
        self.output = ""
        
        self.input1 = Entry(self.wd, justify = "left", relief = "raised", width=50)
        self.input1.place(x=125, y = 80)        #sets up the text input
        
        self.button1 = Button(self.wd, text = "Enter", fg = "blue", command = self.enterText)
        self.button1.place(x=250, y=120)        #sets up the button to submit
        
        
        self.wd.bind("<Return>", self.enterText)        #makes it so hitting the Return key calls the function
        
    def enterText(self):        #called when user is done entering text, saves the text in self.output and quits out of the mainloop
        self.output = self.input1.get()    
        self.wd.quit()    
        
    def startLoop(self):    #once the mainloop ends, the output text will be returned to the startLoop() function
        self.wd.mainloop()
        return self.output
        
        

        
        
    
    
