# task1
import os

path = r"C:\Users\Хаси\Desktop\pp2"
print("Directories:")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
print("\nFiles:")
print(
    [name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]
)
print("\nDirectories and files:")
print([name for name in os.listdir(path)])

# task2
import os

print("Existence:", os.access(r"C:\Users\Хаси\Desktop\pp2\lab6", os.F_OK))
print("Readability:", os.access(r"C:\Users\Хаси\Desktop\pp2\lab6", os.R_OK))
print("Writability:", os.access(r"C:\Users\Хаси\Desktop\pp2\lab6", os.W_OK))
print("Executability:", os.access(r"C:\Users\Хаси\Desktop\pp2\lab6", os.X_OK))

# task3
import os

path = r"C:\Users\Хаси\Desktop\pp2\lab6\builtin.py"
print(os.path.exists(path))

print("File:", os.path.basename(path))

print("Directory portion:", os.path.dirname(path))


# task4
def length(my_file):
    with open(my_file, "r", encoding="utf-8") as f:
        for line, c in enumerate(f):
            pass
    return line + 1


my_file = r"C:\Users\Хаси\Desktop\pp2\lab5\row.txt"
print(length(my_file))

# task5
fruits = ["apple", "pear", "kiwi", "orange"]
with open("fruits.txt", "w") as my_file:
    for i in fruits:
        my_file.write(str(i) + "\n")
r = open("fruits.txt")
print(r.read())

# task6
import string

for i in string.ascii_uppercase:
    with open(i + ".txt", "w") as file:
        file.writelines(i)

# task7
import shutil
shutil.copyfile(r"C:\Users\Хаси\Desktop\pp2\copy.txt", r"C:\Users\Хаси\Desktop\pp2\paste.txt")

#task8
import os
path=r"C:\Users\Хаси\Desktop\pp2\paste.txt"
if os.path.exists(path):
    print("it exists")
    os.remove(path)