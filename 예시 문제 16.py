# 사과 박스 무게의 불량 검사

def solution(weight, boxes):
	answer = 0
	for x in boxes:
		if not weight * 9/10 <= x <= weight * 11/10:
			answer += 1
	return answer

weight = 600
boxes = [653, 670, 533, 540, 660]
ret = solution(weight, boxes)

print("solution 함수의 반환 값은", ret, "입니다.")
