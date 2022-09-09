
""" Digital Clock Using Tkinter """

from tkinter import *
from tkinter.ttk import *
from time import strftime
  

root = Tk()

root.title("Digital Clock")

def Digital():
        
        """ Digital Clock Function code """

        text = strftime("%Y : %m %b : %d %a %I:%M:%S %p")
        
        # another way to use Locale's appropriate date and time representation
        # if you want to display UTC use "%z" 
        #text = strftime(" %c ")

        label.config(text=text)
        label.after(1000,Digital)

label = Label(root,font=("digital" , 50 , "bold") , background="#20bebe" , foreground="#ccddff")
label.pack(anchor="center")

Digital()

root.mainloop()
