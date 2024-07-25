# 시험 등수 구하기


def solution(score):
	answer = []
	sorted_score = sorted(score, reverse=True)
	for sco in score:
		answer.append(sorted_score.index(sco) + 1)
	
	return answer

score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)

print("solution 함수의 반환 값은", ret1, "입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)

print("solution 함수의 반환 값은", ret2, "입니다.")
