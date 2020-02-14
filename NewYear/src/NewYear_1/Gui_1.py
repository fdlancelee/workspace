'''
Created on 2016年1月7日

@author: FUDIAN
'''
# from tkinter import *
# 
# class Applicatoin(from):
#     def __init__(self,mastrt=None):
#         self.pack()
#         self.createWidgets()
#         
#     def createWidegets(self):
#         self.helloLable = Lable(self, text = 'hello,world!')
#         self.helloLable.pack()
#         self.quitButton = Button(self,test='Quit',command=self.quit)
#         self.quitButton.pack()
#         
# app = Applicatoin()
# app.master.title('Hello World')
# app.mainloop()

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()