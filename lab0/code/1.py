#!/usr/bin/python3

data = input("give me your string: ")
print("length of string:", len(data))

data_old = data
data_new = ""
for d in data:
    if d in 'abcdefghijklmnopqrstuvwxyz':
        data_new += chr(ord(d) - 32)
    elif d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        data_new += chr(ord(d) + 32)
    else:
        data_new += d

print("now your string:", data_new)