import os
a = input("Intoduzca el archivo a compilar: ")
os.system("pyinstaller --clean --onefile --windowed {}".format(a))