from collections import deque

def is_palindrome (string):
    d = deque()
    for char in string.replace(" ", "").lower():
        d.append(char)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False     
    return True

print(is_palindrome("Радар"))
print(is_palindrome("Hello world!"))
print(is_palindrome("Я несу гусеня"))
