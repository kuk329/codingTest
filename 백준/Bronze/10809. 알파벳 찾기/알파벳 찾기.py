import string  # 알파벳 가져다 쓰기 위함.

word = input() # 입력받은 문자열

result = [-1]*26 # 알파벳 숫자는 26개

for i in range(len(word)):
    char = word[i]
    for j in range(len(string.ascii_lowercase)):
        lo = string.ascii_lowercase[j]
        if result[j]==-1 and char==lo:
            result[j]=i

print(' '.join([str(num) for num in result]))
