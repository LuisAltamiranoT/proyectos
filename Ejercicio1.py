Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> tk=TK()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tk=TK()
NameError: name 'TK' is not defined
>>> from tkinter import *
>>> tk=Tk()
>>> btn=Button(tk,text="boton")
>>> btn.pack
<bound method Pack.pack_configure of <tkinter.Button object .55227392>>
>>> btn.pack()
>>> 
