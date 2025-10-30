import os

cwd = os.getcwd()
print("Directorio: ", cwd)

print("")
txt_files = [
    f
    for f in os.listdir(
        "/Users/juanpablomanrique/Documents/Repositories/python_exersices/Mi desarrollo"
    )
    if f.endswith(".txt")
]
print("Archivos txt: ", txt_files)
