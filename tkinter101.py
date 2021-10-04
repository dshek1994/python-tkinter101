import tkinter as tk
#Practicing with python gui tkinter

window = tk.Tk()
greeting = tk.Label(
    text="Hello, Tkinter",
    foreground="white",
    background="black",
    width=10,
    height=10
    )

greeting.pack()

window.mainloop()

