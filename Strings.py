text = "Hello World"

print("String:", text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("First character:", text[0])
print("Last character:", text[-1])
print("Substring:", text[0:5])
print("Replace:", text.replace("World", "Python"))

for ch in text:
    print(ch)
