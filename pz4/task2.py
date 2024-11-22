filename = input("Введите имя файла: ")

with open(filename, 'r' ) as file:
    lines = file.readlines()
index = 1
for line in lines:
    print(f"{index} {line.rstrip()}")
    index+=1
with open(filename, 'w') as file:
    index = 1
    for line in lines :
        numline = f"{index} {line}"
        file.write(numline)
        index += 1
