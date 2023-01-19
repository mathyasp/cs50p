text = str(input("Enter text: "))

print(text.translate({ord(i): None for i in "aeiouAEIOU"}))