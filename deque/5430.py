# 문제
# 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

# 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.

# 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 
# 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.

# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.

# 각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.

# 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)

# 다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)

# 전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

# 출력
# 각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.

# 테스트 케이스 갯수 입력받고, 그걸로 반복문 생성
# 명령어 입력 받고, 수의 갯수 입력받고, 배열안에 들어갈 수 입력받는다. 
# 명령어 쪼개서 R,D에 맞는 로직 생성. if not word: print("error") 로 예외 처리 해야 할것으로 예상.
# 결과 출력, 다시 반복문 상단으로 복귀

import sys
from collections import deque
case_num = int(sys.stdin.readline())
reverse_flag = True
error_flag = False
count = 0
for _ in range(case_num):
    command = list(sys.stdin.readline().rstrip())
    length = int(sys.stdin.readline()) 
    array = sys.stdin.readline().rstrip()[1:-1].split(',')
    array = deque(array)
    for i in command:
        if i == 'R':
            if not array :
                error_flag = True
            elif reverse_flag == True:
                reverse_flag = False
            else:
                reverse_flag = True
            count += 1
        elif i == 'D':
            if not array or length == 0:
                error_flag = True
            elif reverse_flag == True:
                array.popleft()
            else:
                array.pop()

    if error_flag == True:
        print("error")
    
    else:    
        if count % 2 != 0: 
            array.reverse()
        print("[", end='') # 개행을 없애기 위해 end = ''를 넣는 것
        for i in range(len(array)):
            if i == len(array)-1:
                print(str(array[i]),end='')
            else:
                print(array[i],end=',')
        print("]")
    
    reverse_flag = True
    error_flag = False
    count = 0
    


            





