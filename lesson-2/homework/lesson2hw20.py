txt = input("")

words = txt.split()


acronym = ''.join(word[0].upper() for word in words)

print(f"Acronym: {acronym}")