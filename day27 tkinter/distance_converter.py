from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx = 50, pady=50)


#Labels
mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_output_label = Label(text="0")
km_output_label.grid(row=1, column=1)

#Entry
mile_input= Entry(width=10)
mile_input.grid(row=0, column=1)

#Button
def button_clicked():
    mile = int(mile_input.get())
    km_output = 1.60934*mile
    km_output_label.config(text=km_output)

cal_button = Button(text="Calculate", command=button_clicked)
cal_button.grid(row=2, column=1)

window.mainloop()