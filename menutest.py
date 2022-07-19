# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 08:34:04 2022

@author: FrizzleFry
"""

import tkinter as tk
from tkinter import ttk

colors = ['#00597c','#a8005c', '#486e4f', '#e94c0a','#007caa','#7b0040', '#aed3e7', '#ffcc00']

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("Test Menu")
        self.geometry('500x400')
        
        
        self.dispFrame = Display(self,self)
        self.dispFrame.pack(side='top',fill='both',expand=1)
    
    
        self.menuFrame = Menu(self, self)
        self.menuFrame.pack(side='bottom')
        
        self.widgetFrame = Widgets(self, self)
        self.widgetFrame.pack(side='bottom')
    
        self.frames = []

    def addFrame(self):
        colorIndex = len(self.frames) % len(colors)
        self.frames.append(Holder(self.dispFrame,self,len(self.frames),bg=colors[colorIndex]))
        cindex = len(self.frames)-1
        
        self.frames[cindex].pack(expand=1, fill='both')
        self.widgetFrame.add(cindex)
        
        return
    
    def resetFrames(self):
        for f in self.widgetFrame.widgets():
            self.frames[f.index].pack_forget()
        self.frames = []
        self.widgetFrame.reset()
        
    def updateFrames(self):             
        for f in self.widgetFrame.widgets():
            
            self.frames[f.index].pack_forget()
            self.frames[f.index].pack(**f.packdata)
        
        
        return

class Frame(tk.Frame):
    def __init__(self, parent, controller, **kwargs):        
        super().__init__(parent, **kwargs)
        self.controller = controller
        self.parent     = parent
        
    
class Menu(Frame):
    def __init__(self,parent,controller, **kwargs):     
        super().__init__(parent, controller, **kwargs)                
        ttk.Button(self,text='+',command=self.controller.addFrame).pack(side='left')
        ttk.Button(self,text='Reset',command=self.controller.resetFrames).pack(side='left')
        
        
class Display(Frame):
    def __init__(self,parent,controller, **kwargs):        
        super().__init__(parent, controller, **kwargs)         


class Holder(Frame):
    def __init__(self,parent,controller,index, **kwargs):
        super().__init__(parent, controller, **kwargs)       
        ttk.Label(self, text='Frame {}'.format(index+1),background=kwargs['bg']).pack()
        
class Widgets(Frame):
    def __init__(self, parent, controller, **kwargs):
        super().__init__(parent, controller, **kwargs)
        self.controlledWidgets = []
        
    def add(self, index):
        self.controlledWidgets.append(WidgetFrame(self,self.controller,index))
        self.controlledWidgets[index].pack(side='left')
    
    def widgets(self):
        for w in self.controlledWidgets:
            yield w
            
    def reset(self):
        for w in self.controlledWidgets:
            w.pack_forget()
        
        self.controlledWidgets = []
    
        
class WidgetFrame(Frame):
    def __init__(self, parent, controller, index, **kwargs):
        super().__init__(parent, controller, **kwargs)
        
        self.packdata = {
                'side': 'top',
                'expand': 1,
                'fill': 'both',
                'anchor': tk.NW,
            }
        
        self.index = index
        ttk.Label(self,text='Frame {}'.format(index+1)).pack()
        
        self.sidestr = tk.StringVar(self)
        self.sidestr.set('top')
        
        self.expvar = tk.StringVar(self)
        self.expvar.set('True')
        
        self.fillvar = tk.StringVar(self)
        self.fillvar.set('both')
        
        self.anchvar = tk.StringVar(self)
        self.anchvar.set(tk.NW)
        
        ttk.OptionMenu(self, self.sidestr, 'top', 'left', 'bottom', 'right', 'top', command=self.updatePackSide).pack()
        ttk.OptionMenu(self, self.expvar, 'True', 'True', 'False', command=self.updateExpand).pack()
        ttk.OptionMenu(self, self.fillvar, 'both', 'x', 'y', 'none', 'both', command=self.updateFill).pack()
        ttk.OptionMenu(self, self.anchvar, tk.NW, tk.NW, tk.N, tk.NE, tk.E, tk.SE, tk.S, tk.SW, tk.W, command=self.updateAnchor).pack()
        
    def updatePackSide(self, v):
        self.packdata['side'] = self.sidestr.get()
        self.controller.updateFrames()
    
    def updateExpand(self, v):
        self.packdata['expand'] = self.expvar.get()
        self.controller.updateFrames()
        
    def updateFill(self, v):
        self.packdata['fill'] = self.fillvar.get()
        self.controller.updateFrames()
        
    def updateAnchor(self, v):
        self.packdata['anchor'] = self.anchvar.get()
        self.controller.updateFrames()


if __name__ == '__main__':
    app = App()
    app.mainloop()