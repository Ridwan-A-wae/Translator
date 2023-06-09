# -*- coding: utf-8 -*-

from cgitb import text
from tkinter import *
from tkinter.font import Font
from googletrans import Translator

# ขนาดหน้าจอ
root = Tk()
font = Font(family="TH Sarabun New", size=12)  # หรือเลือกฟอนต์ที่รองรับภาษาไทย
root.title("Google Translate (EN-TH)")
root.geometry('530x300')
root.maxsize(530,300)
root.minsize(530,300)



# widget
lable = Label(text="English - Thai",font=("Arial",25,"bold"))
lable.place(x=150,y=20)

# เก็บข้อความภาษาอังกฤษ
text1 = Text(root,width=30,height=10)
text1.place(x=10,y=70)

# เก็บข้อมูลภาษาไทย
text2 = Text(root,width=30,height=10)
text2.place(x=260,y=70)

def tranSlate():
    message = text1.get("1.0","end-1c")
    translator = Translator()
    output = translator.translate(text=message,src="en",dest="th")
    text2.insert('end',output.text)

def clear():
    text1.delete(1.0,'end')
    text2.delete(1.0,'end')

# ปุ่ม
btnTrans = Button(root,text="แปลภาษา",command=tranSlate).place(x=180,y=250)
btnClear = Button(root,text="เคลียร์",command=clear).place(x=280,y=250)

root.mainloop()