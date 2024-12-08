doc = open("wordtest.docx", "rb").read()

for char in doc:
    print(chr(char), end="")