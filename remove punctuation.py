import string
s ="hello, world! Python is #1!"
clean =''.join(c for c in s if c not in string.punctuation)
print(clean)