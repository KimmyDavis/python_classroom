from os import popen
combined = ""
for lne in popen("dir"):
    if lne.rstrip()[-2:] == "py":
        fname = lne.split()[-1]
        if fname == "morefile.py": continue
        print("\n\n"+"-"*10+fname+"-"*10+"\n")
        filestr = ""
        for line in open(fname):
            print(line, end="")
            filestr += line
        print()
        print("______________RESULTS!______________")
        try:
            exec(filestr)
        except:
            print("ERROR!")

