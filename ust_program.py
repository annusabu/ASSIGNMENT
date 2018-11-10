import re
def frame(words):
    size = max(len(word) for word in words)
    print('*' * (size + 4))
    for word in words:
        print('* {:<{}} *'.format(word, size))
    print('*' * (size + 4))
str=raw_input("Enter the string")
reg=re.compile('^[a-zA-z\s\.]+$')
if reg.match(str):
    words=str.split()
    frame(words)
else:
    print("Please enter string without special characters and numbers")
