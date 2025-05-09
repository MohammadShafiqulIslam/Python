import tkinter as tk

root = tk.Tk()
root.title("Student Management System")

tk.Label(root, text="Student Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Button(root, text="Add Student", command=add_student).grid(row=1, column=0, columnspan=2)

root.mainloop()
