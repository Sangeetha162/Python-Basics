file = open("sample.txt", "w")

file.write("Hello, Python File Handling!")

file.close()

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
