# 사다리 게임의 승리자를 구해주세요!

def solution(ladders, win):
	answer = 0
	player = [1, 2, 3, 4, 5, 6]
	for e in ladders:
		temp = player[e[0]-1]
		player[e[0]-1] = player[e[1]-1]
		player[e[1]-1] = temp
	answer = player[win-1]
	return answer

ladders = [[1, 2], [3, 4], [2, 3], [4, 5], [5, 6]]
win = 3
ret = solution(ladders, win)

print("solution 함수의 반환 값은", ret, "입니다.")
