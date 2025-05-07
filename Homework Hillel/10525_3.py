import string

text = input("Введіть рядок: ")
text = "".join(char for char in text if char not in string.punctuation)
words = text.split()
hashtag = '#' + ''.join(word.capitalize() for word in words)
hashtag = hashtag[:140]

print(hashtag)