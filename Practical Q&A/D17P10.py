import os

filename = "copy_todo.txt"
confirm = input(f"Do you really want to delete {filename}? (yes/no): ")

if confirm.lower() == "yes":
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} has been deleted.")
    else:
        print(f"{filename} does not exist.")
else:
    print("File deletion canceled.")
