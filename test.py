import tkinter as tk

def get_user_input():
    user_input = entry.get()
    result_label.config(text=f"You entered: {user_input}")

# Create the main window
root = tk.Tk()
root.title("User Input Example")

# Entry widget for user input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Button to trigger getting user input
submit_button = tk.Button(root, text="Submit", command=get_user_input)
submit_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
