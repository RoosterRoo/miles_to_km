from tkinter import *

window = Tk()
window.title("Miles to Km")
window.config(padx=20, pady=20)


def miles_to_km_calc():
    miles_in = miles_input.get()
    if not miles_in:
        return
    miles = float(miles_input.get())
    km = miles * 1.609
    km_output.config(text=f"{km}")


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

miles_to_km_calculate_button = Button(text="Calculate", command=miles_to_km_calc)
miles_to_km_calculate_button.grid(column=1, row=2)

window.mainloop()
