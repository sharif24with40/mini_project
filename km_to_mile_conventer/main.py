from tkinter import *

def miles_to_km():
    # Get the value from the input field, convert it to float and calculate the kilometers
    miles = float(miles_input.get())
    km = miles * 1.60934 
    # Update the kilometer_label with the calculated value
    kilometer_label.config(text=f"{km:.2f}")

# Create the main window
window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=25, pady=25)

# Create and place the input field for miles
miles_input = Entry(window, width=8)
miles_input.grid(column=1, row=0)

# Create and place the miles label
miles_label = Label(window, text="Miles", padx=10, pady=10)
miles_label.grid(column=2, row=0)

# Create and place the 'is equal to' label
is_equal_label = Label(window, text="is equal to", padx=10, pady=10)
is_equal_label.grid(column=0, row=1)

# Create and place the kilometers result label
kilometer_label = Label(window, text="0 Km", padx=10, pady=10)
kilometer_label.grid(column=1, row=1)

# Create and place the calculate button
calculate_button = Button(window, text="Calculate", command=miles_to_km)
calculate_button.grid(column=2, row=1)

# Run the main event loop
window.mainloop()
