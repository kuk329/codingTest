count_remove_zero = 0
repeat = 0


def solution(string):
    global repeat
    answer = []
    
    while True:
        if string =="1":
            break
        repeat += 1
        if is_zero_in_binary(string):
            string = remove_zero(string)

        string = change_decimal_to_binary(string)

    answer.append(repeat)
    answer.append(count_remove_zero)

    return answer


def remove_zero(string):
    global count_remove_zero
    # arr = list(string)  # 문자열을 문자 배열로 쪼갬
    # n = len(arr)
    # #  count_remove_zero = 0 # 제거한 0 의 개수
    # for i in range(n):
    #     if arr[i] == "0":
    #         del arr[i]
    #         count_remove_zero += 1
    count_remove_zero+=string.count('0')
    new_string=string.replace('0','')

    return new_string


def change_decimal_to_binary(string):
    decimal = len(string)  # 문자열의 길이를 저장
    binary = []
    while decimal != 0:
        remain = decimal % 2
        decimal = decimal // 2
        binary.append(str(remain))

    binary.reverse()
    return ''.join(binary)


def is_zero_in_binary(string):
    for s in string:
        if s == "0":
            return True
    return False
