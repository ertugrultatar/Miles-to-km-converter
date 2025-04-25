from tkinter import *


window = Tk()
window.title("Miles to Km Converter")

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    km_result_label.config(text=f"{km}")


miles_input = Entry(width=6)
miles_input.grid(row=0, column=1)


miles_label = Label(text="Miles")
miles_label.grid(row=0, column=3, padx=10)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0, padx=10)


km_result_label = Label(text="0")
km_result_label.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)




















window.mainloop()