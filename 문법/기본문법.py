#리스트 컴프리헨션
# #lst = [[0*m for _ in range(n)]] # N,M의 행렬 생성
# #set자료형을 활용해서 remove.all
# #tuple자료형 활용 : 서로 다른 성질 묶을 경우, 데이터 나열 해싱
# #사전과 집합자료형은 index가 없기 때문에 빅(1)의 시간복잡도로 조회

#f-string
answer = 7
print(f"answer is {answer} 입니다")

class oneline_if:
    #조건문 간소화
    if answer>=7 : result = "success"
    else : result = "fail"

    result = "success" if answer>=7 else "fail"

#람다식

#라이브러리
# #내장함수
# #itertools 조합 순열
# #heapq 우선순위 큐
# #bisect 이진탐색
# #collections 덱 카운터
# #math 필수적 수학기능 gcd lcm

#내장 종류
# #sum() min() max() eval() sorted(lst) sort()
