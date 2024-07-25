# 위험한 지역 몇개인지 알려주기


def solution(height):
	count = 0
	check = False
	location = [[-1, 0], [0, -1], [1, 0], [0, 1]]
	
	for row in range(len(height)):
		for col in range(len(height)):
			for loc in location:
				if 0 <= row + loc[0] < len(height) and 0 <= col + loc[1] < len(height):
					if height[row][col] < height[row + loc[0]][col + loc[1]]:
						check = True
					else:
						check = False
						break
			if check:
				count += 1
	return count

height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

print("solution 함수의 반환 값은", ret, "입니다.")
