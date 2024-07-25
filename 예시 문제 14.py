# 가장 오래 일한 사람을 구해주세요.


def solution(time_table, n):
	time = [0 for _ in range(n)]
	
	for idx in range(len(time_table)):
		time[idx%n] += time_table[idx]
	return max(time)

time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
