from tkinter import *

class Gui:
    def __init__(self):
        self.wd = Tk()
        self.wd.title("databaseGUI")
        self.wd.geometry("500x200")
        
        self.output = ""
        
        self.input1 = Entry(self.wd, justify = "left", relief = "raised", width=50)
        self.input1.place(x=125, y = 80)
        
        self.button1 = Button(self.wd, text = "Enter", fg = "blue", command = self.enterText)
        self.button1.place(x=250, y=120)
        
    def enterText(self):
        self.output = self.input1.get()    
        self.wd.quit()    
        
    def startLoop(self):
        self.wd.mainloop()
        return self.output
        
        

        
        
    
    
