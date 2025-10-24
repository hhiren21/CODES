import tkinter as tk
from time import strftime

def time():
    """
    Updates the clock display with the current time.
    """
    # Get current time in HH:MM:SS format
    string = strftime('%H:%M:%S %p')
    
    # Update the label with the new time
    lbl.config(text=string)
    
    # Schedule the 'time' function to run again after 1000 milliseconds (1 second)
    lbl.after(1000, time)

# 1. Initialize the main window
root = tk.Tk()
root.title("Digital Clock")

# 2. Create the label for the time display
lbl = tk.Label(
    root,
    font=('calibri', 40, 'bold'), # Font and size
    background='black',          # Background color
    foreground='cyan'            # Text color
)

# 3. Place the label in the center of the window
lbl.pack(anchor='center')

# 4. Start the time update loop
time()

# 5. Run the main tkinter event loop
root.mainloop()
