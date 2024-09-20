from tkinter import *
from tkinter import ttk
from forecast_finder import forecast_finder


def main():
    # Create the main application window
    root = Tk()
    root.title('Forecast Finder')  # Set the title of the window
    root.configure(bg='cyan2')  # Set the background color

    # StringVar to hold user input for location and number of days
    location_selected = StringVar()
    num_days_selected = IntVar()

    # Configure the styles for the widgets
    style = ttk.Style()
    style.configure('TFrame', background='cyan2')
    style.configure('TLabel', background='cyan2')
    style.configure('TEntry', background='cyan2')

    # Frame for location input
    location_frame = ttk.Frame(root, padding=10)
    location_frame.grid()
    ttk.Label(location_frame, background='cyan2', text='Enter a zipcode or city name: ').grid(column=0, row=0)
    # Entry widget for user to input location
    location_entry = ttk.Entry(location_frame, textvariable=location_selected)
    location_entry.grid(column=3, row=0)

    # Frame for number of days input
    num_days_frame = ttk.Frame(root, padding=10)
    num_days_frame.grid()
    ttk.Label(num_days_frame, background='cyan2', text='Enter the number of days: ').grid(column=0, row=1)
    # Entry widget for user to input number of days
    num_days_entry = ttk.Entry(num_days_frame, textvariable=num_days_selected)
    num_days_entry.grid(column=2, row=1)

    # Text widget to display the forecast output
    forecast_output = Text(root, height=15, width=50, bg='cyan2')
    forecast_output.grid(column=0, row=6, columnspan=4, pady=10)

    # Placeholder label for spacing
    ttk.Label(num_days_frame, text='').grid(row=3)

    def save_inputs():
        # Retrieve user inputs for location and number of days
        location = location_selected.get()
        num_days = num_days_selected.get()
        print(f"Location: {location} \nNumber of Days: {num_days}")
        
        # Call the forecast_finder function and retrieve the forecast
        forecast_result = forecast_finder(location, num_days)
        
        # Clear previous output and insert the new forecast result
        forecast_output.delete(1.0, END)
        forecast_output.insert(END, forecast_result)

    # Button to submit the inputs and fetch the forecast
    ttk.Button(num_days_frame, text='Submit', command=save_inputs, padding=2).grid(column=2, row=5)

    # Start the main event loop of the application
    root.mainloop()


if __name__ == "__main__":
    main()  # Run the main function when the script is executed
