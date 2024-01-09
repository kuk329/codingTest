d = {"[": "]", "(": ")"}


def go(string):
    stack = []
    result = "yes"
    for s in string:
        if s == "[" or s == "(":
            stack.append(s)
        if s == "]" or s == ")":
            if not stack:
                result = "no"
                break
            else:
                out = stack.pop()
                if d[out] != s:
                    result = "no"
                    break

    if stack:
        result = "no"

    print(result)


while True:
    string = input()
    if string == ".":
        break

    go(string)
