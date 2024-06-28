from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.grid(row=0, column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

converted_km_label = Label(text="0")
converted_km_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


def click_button():
    miles = float(mile_input.get())
    converted_km = round(miles * 1.609, 2)
    converted_km_label.config(text=f"{converted_km}")


button = Button(text="Calculate", command=click_button)
button.grid(row=2, column=1)

window.mainloop()
