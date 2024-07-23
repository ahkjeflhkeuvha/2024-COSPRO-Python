# k번째로 작은 수
def solution(arr, k):
    kArr = []
    
    for i in arr:
        kArr.extend(i)
    kArr.sort()
    return kArr[k-1]
