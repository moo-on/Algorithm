from collections import deque

#2->10
def binary_to_decimal(binary):
    decimal = 0
    #2진수를 리스트에 하나씩 저장
    temp = list(str(binary))
    length = len(temp)
    #각 자리가 1이라면 2의 승수만큼 더해줌
    for i, e in enumerate(temp):
        if e == '1': decimal += 2**(length -1 - i)
    return int(decimal)
print(binary_to_decimal('1011'))

#10->2
def decimal_to_binary(decimal):
	temp = deque()
	#10진수를 2로 나눈다.
	q,r = divmod(int(decimal), 2)
	#나머지를 하나씩 저장
	temp.appendleft(r)
	#몫이 0이 될 때 까지 나머지 저장 해준다.
	while q != 0:
		q,r = divmod(q, 2)
		temp.appendleft(r)
	#하나 씩 저장한 나머지들을 합쳐서 출력
	binary = ''.join(list(map(str, temp)))
	return str(binary)
print(decimal_to_binary(11))

#2->16
def binary_to_hexadecimal(binary):
    binary = list(str(binary))
    #배열의 크기 4로 맞추기
    for _ in range(4 - len(binary)%4):
        binary.insert(0, 0) 
    answer = deque()
    t = 0
    temp = 0
    #2진수를 하나씩 빼주면서 4개의 스택이 쌓이면 16진수로 변환 후 하나씩 붙여준다
    while binary:
        n = int(binary.pop())
        if n == 1:
            temp += 2**t
        t+=1
        if t == 4:
            if temp >=10:
                #A = 65이기에, 55 더한 후 아스키코드로 변환
                temp += 55
                answer.appendleft(chr(temp))
            else:answer.appendleft(str(temp))
            t = 0
            temp = 0
    #16진수로 표기 해준 후 리턴
    answer = ''.join(answer).lstrip('0')
    answer = ''.join(['0x',answer])
    return str(answer)
print(binary_to_hexadecimal('10111111'))

#16->2
def hexadecimal_to_binary(hexadecimal):
    answer = []
    #0x제거
    temp = list(hexadecimal[2:])
    for e in temp:
        if e.isalpha(): n = ord(e) - 55
        else: n = int(e)
        n = str(decimal_to_binary(n))
        while len(n) != 4:
            n=''.join(['0', n])
        answer.append(n)
    answer = ''.join(answer)
    answer = answer.lstrip('0')
    return str(answer)
print(hexadecimal_to_binary('0xBF'))

#10->16
def decimal_to_hexadecimal(decimal):
    answer = deque()
    temp = deque()
    #10진수를 16로 나눈다.
    q,r = divmod(int(decimal), 16)
    #나머지를 하나씩 저장
    temp.appendleft(r)
    #몫이 0이 될 때 까지 나머지 저장 해준다.
    while q != 0:
        q,r = divmod(q, 2)
        temp.appendleft(r)
    for e in temp:
        if e >=10:
                #A = 65이기에, 55 더한 후 아스키코드로 변환
                e += 55
                answer.appendleft(chr(e))
        else:answer.appendleft(str(e))
        
    #하나 씩 저장한 나머지들을 합쳐서 출력
    answer.appendleft('0x')
    hexadecimal = ''.join(answer)
    return str(hexadecimal)
print(decimal_to_hexadecimal(10))

#16->10
def hexadecimal_to_decimal(hexadecimal):
    answer = 0
    #0x제거
    hexa = list(hexadecimal[2:].upper())
    length = len(hexa)
    #각 자릿수에 맞게 16의 승수를 곱해서 더해준다.
    for i,e in enumerate(hexa):
        if e.isalpha(): answer += (ord(e)-55)*(16**(length-1-i))
        else: answer += (16**(length-1-i))*int(e)
    return int(answer)
print(hexadecimal_to_decimal('0xBF'))