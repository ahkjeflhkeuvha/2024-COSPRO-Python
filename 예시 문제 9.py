# 남은 재료로 주스 만들기 

def solution(num_apple, num_carrot, k):
	answer = 0

	if num_apple < (3 * num_carrot):
		answer = num_apple // 3 # 3
	else:
		answer = num_carrot

	num_apple -= answer * 3 # num_apple = 1
	num_carrot -= answer # num_carrot = 2
	# answer = 3

	i = 0
	k = k - (num_apple + num_carrot) # k = 1

	while k > 0:
		if i % 4 == 0:
			answer = answer - 1 # 4
		i = i + 1 # 1
		k = k - 1 # 0

	return answer

num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)

print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)

print("solution 함수의 반환 값은", ret2, "입니다.")
