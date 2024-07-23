# 배열의 순서 뒤집기

def solution(arr):
	left, right = 0, len(arr)-1
	while left < right:
		arr[left], arr[right] = arr[right], arr[left]
		left += 1
		right -= 1
	return arr

arr = [1, 4, 2, 3]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")
