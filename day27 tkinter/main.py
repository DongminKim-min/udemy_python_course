from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height= 300)
window.config(padx=50, pady=50) # make space on the edges

'''use <pack / place / grid> to add a widget on a window'''
#pack: simply puts a widget
#place: precisely puts a widget to the according x, y coordinates
#grid: using grid

def button_clicked():
    print("I got clicked")
    my_label.config(text= input.get())

#Label
my_label = Label(text="I Am a Label", font=("Ariel", 24, "bold")) #font는 tuple임
my_label["text"] = "New Text"
# my_label.config(text= "New Text") <- This also works
# my_label.pack() <- default location(center)에 label 위치
# my_label.pack(side= "left")
my_label.grid(row=0, column=0)
my_label.config(padx=20, pady=20) #make space on the edges of the widget

#Button
button = Button(text= "Click Me", command= button_clicked)
button.grid(row=1, column=1)

new_button = Button(text= "Newbie")
new_button.grid(row=0, column=2)

#Entry
input = Entry(width=20)
input.grid(column=3, row=3)









window.mainloop()
