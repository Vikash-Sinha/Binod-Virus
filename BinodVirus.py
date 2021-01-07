# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 14:51:14 2020

@author: vikas
"""
import os
from tkinter import *
import time
from tkinter.ttk import Progressbar
root=Tk()
def frames():
    global prog
    global frm
    frm=LabelFrame(root,text='Deleting Files')
    frm.grid(row=2,column=0,columnspan=5,pady=20)
    prog=Progressbar(frm,orient=HORIZONTAL,length=500,mode='determinate')
    prog.pack()
    return

def progval(i,n):
    while(i<n):
         prog['value']+=5
         frm.update_idletasks()
         time.sleep(1)
         i+=1
             
    return

def virus():
    frames()
    progval(0,10)
        
    for path,dirs,file in os.walk('//home//vikash//Windows files and folder//Vikash Sinha//d drive//ludo//vks'):
    
     
      for p in file:
          pat=path+'//'+p
          os.remove(pat)
      for d in dirs:
             patd=path+'//'+d
             for pa in file:
                 try:
                     paa=patd+'//'+pa
                     print(paa)
                     os.remove(paa)
                 except:
                    pass
   
         
    progval(0,10)
    messagebox.showwarning(title='Binod Virus', message='Virus Run Sucessfully')
    return

def click():
    t=messagebox.askokcancel(title='Binod Virus', message='This virus will delete your all files')
    if t:
     t=messagebox.askyesno(title='Binod Virus', message='Are you Sure')
     if t:
        virus() 
    
    print(t)
root.geometry('650x400')
root.title('Binod Virus')
l1=Label(root,text='Binod Virus Desing By Vikash Sinha', font='Arial 26 bold',bg='red',fg='blue',padx=10,pady=12,width=31)
l1.grid(row=0,column=0,columnspan=5,pady=20)
b1=Button(root,text='Run The Virus',font='Arial 20 bold',bg='red',fg='white',command=click)
b1.grid(row=1,column=2,pady=20)
root.mainloop()

