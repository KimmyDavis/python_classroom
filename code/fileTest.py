myfile = open("myfile.txt", "w")
myfile.write("Hello file world!\n")
myfile.close()

mynewfile = open("myfile.txt", "r")
for line in mynewfile:
    print(line, end="")