
code = []
while True:
    sentence = input()
    if sentence=="END":
        break
    code.append(sentence)


for s in code:
    print(s[::-1])
