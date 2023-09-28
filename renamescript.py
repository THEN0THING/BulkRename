import os

'''
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Rename Files")
root.geometry("500x300")

Label(root, text="New Filename:").place(x=50, y=40)
Label(root, text="File Extension:").place(x=50, y=100)

entry1 = Entry(root, bd=5)
entry2 = Entry(root, bd=5)

entry1.place(x=120, y=40)
entry2.place(x=120, y=100)

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)
'''
'''Button(root, text="Ok", command=renameType).place(x=150, y=150)'''
'''root.mainloop()'''
'''print(entry1.get())'''

'''
    '''


def renamio(filenames, params):

    nameto = input("rename to:\n")

    for filename in filenames:

        extension = os.path.splitext(filename)[1]
        new_name = os.path.join(os.path.dirname(filename), (nameto + extension))

        print("Renaming:", filename, "to", new_name)

        # Rename the file
        os.rename(filename, new_name)
    input()
