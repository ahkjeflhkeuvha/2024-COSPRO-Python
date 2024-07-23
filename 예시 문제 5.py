# 시작 날짜와 끝 날짜 사이의 날짜 구하기

def func_a(month, day):
	month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	total = 0;
	for i in range(month - 1):
		total += month_list[i]
	total += day
	return total - 1

def solution(start_month, start_day, end_month, end_day):
	start_total = func_a(start_month, start_day)
	end_total = func_a(end_month, end_day)
	return end_total - start_total

start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

print("solution 함수의 반환 값은", ret, "입니다.")
