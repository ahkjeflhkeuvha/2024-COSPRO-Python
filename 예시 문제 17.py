# 음료수 마시기

def solution(money, price, n):
	answer = 0
	empty_bottle = answer = money // price
	while n <= empty_bottle:
		empty_bottle = empty_bottle - n
		answer += 1
		empty_bottle += 1
	return answer

money1 = 8
price1 = 2
n1 = 4
ret1 = solution(money1, price1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

money2 = 6
price2 = 2
n2 = 2
ret2 = solution(money2, price2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
