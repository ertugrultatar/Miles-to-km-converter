from tkinter import *  # Import everything from tkinter to use GUI components

# Create the main window and set its title
window = Tk()
window.title("Miles to Km Converter")

# Function to convert miles to kilometers
def miles_to_km():
    miles = float(miles_input.get())  # Get the value from the input field and convert it to a float
    km = round(miles * 1.609, 2)  # Convert miles to kilometers (1 mile = 1.609 km), rounded to 2 decimal places
    km_result_label.config(text=f"{km}")  # Update the label with the result in kilometers

# Input field for miles
miles_input = Entry(width=6)
miles_input.grid(row=0, column=1)

# Labels for miles and kilometers
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=3, padx=10)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0, padx=10)

km_result_label = Label(text="0")
km_result_label.grid(row=1, column=1)

km_label = Label(text="km")
km_label.grid(row=1, column=2)

# Button to trigger the conversion
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)

# Run the main event loop
window.mainloop()
