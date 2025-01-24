from collections import deque

def solution(order):
    answer = 0
    truck = []
    # 택배 순서 : order
    tmp = [i + 1 for i in range(len(order))]
    belt = deque(tmp)
    extra_belt = []
    order_idx = 0
    while True:
        if order_idx == len(order):
            break

        if belt: # 벨트 위에 아직 택배가 존재할 경우
            if order[order_idx] == belt[0]:
                truck.append(order[order_idx])
                order_idx += 1
                belt.popleft()
            elif order[order_idx] > belt[0]:
                extra_belt.append(belt.popleft())
            else:
                if extra_belt:
                    if extra_belt[-1] == order[order_idx]:
                        truck.append(extra_belt.pop())
                        order_idx += 1
                    else:
                        break
                else:
                    break
        else: # 벨트 위에 택배가 없는데 아직 모든 택배를 실지 않은 경우
            if extra_belt[-1] == order[order_idx]:
                truck.append(extra_belt.pop())
                order_idx += 1
            else:
                break


    answer = len(truck)
    return answer