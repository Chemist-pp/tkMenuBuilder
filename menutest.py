# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 08:34:04 2022

@author: FrizzleFry
"""

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Test Menu")
        self.geometry('500x400')
        
        self.menuFrame = Menu(self, self)
        self.menuFrame.pack(side='bottom')
        
        self.dispFrame = Display(self,self)
        self.dispFrame.pack(side='top')
    
class Frame(tk.Frame):
    def __init__(self, parent, controller):        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        
    
class Menu(Frame):
    def __init__(self,parent,controller):     
        Frame.__init__(self, parent, controller)                
        ttk.Label(self, text='Hi').pack()
        
        
class Display(Frame):
    def __init__(self,parent,controller):        
        Frame.__init__(self, parent, controller)        
        ttk.Label(self, text="Show Menu Here").pack()                                 



if __name__ == '__main__':
    app = App()
    app.mainloop()