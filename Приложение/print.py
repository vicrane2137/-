from tkinter import*
from tkinter import ttk
root = Tk()
root.title("Планировщик задач")
root.geometry("460x520")
label = Label(text="Hello World")
python_logo = PhotoImage(file="task-planner-banner.png")
ttk.Entry().pack(anchor=NW, padx=8, pady=8)
label = ttk.Label(image=python_logo, compound="top")

label.pack()
root.mainloop()