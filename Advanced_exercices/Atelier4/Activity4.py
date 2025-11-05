import csv
def multiplication():
    list = []
    x = 1
    while x <= 10:
        list.append(f"La table de multiplication de {x}: ")
        for i in range(1,11, 1):
            list.append(f"{x:02}{" "*4}*{" "*4}{i:02}{" "*4}={" "*4}{x * i:02}")
        x += 1
    return list
table = multiplication()
with open("Activity4.txt", "a+") as file:
    for line in table:
        file.write(line + "\n")
