import tkinter as tk

def on_button_click():
    user_text = entry.get()
    label.config(text=f"Hello, {user_text}!")

root = tk.Tk()
root.title("Hello World App")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(frame, text="Enter your name:", font=("Arial", 14))
label.grid(row=0, column=0)

entry = tk.Entry(frame, font=("Arial", 14))
entry.grid(row=0, column=1)

button = tk.Button(frame, text="Submit", font=("Arial", 14), command=on_button_click)
button.grid(row=1, column=1, sticky="e")

root.mainloop()