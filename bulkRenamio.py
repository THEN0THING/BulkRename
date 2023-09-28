import os
import sys

filenames = sys.argv[1:]

print("Hello this program will rename all the files selected to the name you provide. It will add am index")
nameto = input("Rename files to (Do not include extension):\n")

for filename in filenames:

    extension = os.path.splitext(filename)[1]
    new_name = os.path.join(os.path.dirname(filename), (nameto + str(filenames.index(filename)) + extension))

    print("Renaming:", filename, "to", new_name)

    os.rename(filename, new_name)
    input()
