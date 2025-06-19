s= "Python is a powerful scripting language"
no_vowel = ''.join(c for c in s if c.lower() not in 'aeiou')
print("String without vowels:", no_vowel)
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Upper:", upper, "| Lower:", lower)
