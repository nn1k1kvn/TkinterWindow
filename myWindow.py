#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Модальные окна в  Tkinter
мануалы тут http://www.russianlutheran.org/python/nardo/nardo.html#102

'''

# импортирование модулей python
from Tkinter import *

'''
Лучше так

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

'''

# класс главного окна
class main:
  def __init__(self, master):
    self.master = master
    self.master.title('main')
    self.master.geometry('100x100+200+150')
    



    self.exit_button = Button(self.master,
                                text = 'exit',
                                command = self.exitMethod)
    self.exit_button.pack(side=BOTTOM)

    self.button = Button(self.master,
                         text = 'dialog',
                         command = self.openDialog)
    self.button.pack(side = BOTTOM)


    self.master.protocol('WM_DELETE_WINDOW',
                         self.exitMethod)
    self.master.mainloop()

  def openDialog(self):
    self.dialog = dialog(self.master)
    self.dialog.go(u'Привет медвед')

  def exitMethod(self):
    self.dialog = yesno(self.master)
    self.myMssg = 'Do you want to exit?'
    self.returnValue = self.dialog.go(message = self.myMssg)
    if self.returnValue:
      self.master.destroy()

# класс дочернего окна
class dialog:
  def __init__(self, master):
    self.top = Toplevel(master)
    self.top.title('dialog')
    self.top.geometry('+300+250')
    self.frame = Frame(self.top)
    self.frame.pack(side = TOP)
    self.frame.scroll =  Scrollbar(self.frame)
    self.frame.scroll.pack(side='right', fill='y')
    self.frame.text = Text(self.frame, yscrollcommand=self.frame.scroll.set) 
    self.frame.text.pack(side='left', fill='both', expand=YES)
    self.exit_button = Button(self.top,
                                text = 'exit',
                                command = self.exit)
    self.exit_button.pack(side=BOTTOM, ipadx=30)
    self.top.protocol('WM_DELETE_WINDOW', self.exit)

  
  def go(self, myText = '',):
    self.frame.text.insert('0.0', myText)
    self.top.grab_set()
    self.top.focus_set()
    self.top.wait_window()
   

  def exit(self):
    self.top.destroy()   

# класс диалогового окна выхода
class yesno:
  def __init__(self, master):
    self.slave = Toplevel(master)
    self.frame = Frame(self.slave)
    self.frame.pack(side = BOTTOM)
    self.yes_button = Button(self.frame, 
                             text = 'yes', 
                             command = self.yes)
    self.yes_button.pack(side = LEFT)
    self.no_button = Button(self.frame, 
                            text = 'no', 
                            command = self.no) 
    self.no_button.pack(side = RIGHT)   
    self.label = Label(self.slave)
    self.label.pack(side = TOP,
                    fill = BOTH,
                    expand = YES)
    self.slave.protocol('WM_DELETE_WINDOW', self.no)

  def go(self, title = 'question', 
               message = '[question goes here]', 
               geometry = '200x70+300+265'):
    self.slave.title(title)
    self.slave.geometry(geometry)
    self.label.configure(text = message)
    self.booleanValue = TRUE
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()
    return self.booleanValue

  def yes(self):
    self.booleanValue = TRUE
    self.slave.destroy()

  def no(self):
    self.booleanValue = FALSE
    self.slave.destroy()       

     

# создание окна
root = Tk()

# запуск окна
main(root)
