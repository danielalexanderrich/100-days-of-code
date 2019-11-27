# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:03:03 2019

@author: dan
"""

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master= None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        
    def create_widgets(self):
        self.left = tk.Button(self)
        self.left["text"] = "Move left"
        self.left["command"] = self.move_left
        self.left.pack(side="left")
        
        self.right = tk.Button(self)
        self.right["text"] = "Move right"
        self.right["command"] = self.move_right
        self.right.pack(side = "right")
        
         
        self.quit = tk.Button(self, text="QUIT", fg="red",
                           command=self.master.destroy)
        self.quit.pack(side="bottom")
     
    
    def move_left(self):
        print("moved left")
    
    def move_right(self):
        print("moved right")
        
root = tk.Tk()
app = Application(master = root)
app.mainloop()
