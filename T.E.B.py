def process(s):
    result = []
    for char in s:
        if char != '#':
            result.append(char)
        elif result:
            result.pop()
    return "".join(result)

def backspace_compare(S, T):
    return process(S) == process(T)

s = "ab#c"
t = "ab#c"

print(backspace_compare(s, t), "\n")
