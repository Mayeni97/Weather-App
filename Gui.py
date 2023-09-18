import customtkinter as ctk

# Create the root window
root = ctk.CTk()
root.geometry("500x350")

# Define the login function
def login():
    print("Test")

# Create a frame and pack it into the root window
frame = ctk.CTkFrame(root)
frame.pack()

# Create a label, entry1, entry2, button, and checkbox and pack them into the frame
label = ctk.CTkLabel(frame, text="Login")
label.pack()

entry1 = ctk.CTkEntry(frame)
entry1.pack()

entry2 = ctk.CTkEntry(frame)
entry2.pack()

button = ctk.CTkButton(frame, text="Login", command=login)
button.pack()

checkbox = ctk.CTkCheckBox(frame, text="Remember me")
checkbox.pack()

# Start the main loop for the root window
root.mainloop()