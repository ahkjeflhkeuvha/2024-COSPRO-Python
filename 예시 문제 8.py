# 체조 선수의 점수 구해주기

def solution(scores):
	scores.sort()
	return int(sum(scores[1:len(scores) - 1])/(len(scores) - 2))

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

print("solution 함수의 반환 값은", ret2, "입니다.")
