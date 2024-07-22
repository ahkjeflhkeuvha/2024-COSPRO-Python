scores = [2024, 7, 22, 3, 4]

def sum_list(datas):
    tot = 0
    for i in datas:
        tot += i
    return tot

def max_list(datas):
    maxData = datas[0]
    for i in datas:
        if(maxData < i):
            maxData = i
    return maxData

def min_list(datas):
    minData = datas[0]
    for i in datas:
        if(minData > i):
            minData = i
    return minData

def average_list(datas):
    sumData = sum(datas)
    sumLen = len(datas)
    return sumData/sumLen

def count_odd(datas):
    tot = 0
    for i in datas:
        if i%2 == 0:
            tot += i
    return tot

def make_list(num):
    returnList = []
    for i in range(0, num):
        returnList.append(0)
    return returnList

print(sum_list(scores))
print(max_list(scores))
print(min_list(scores))
print(average_list(scores))
print(count_odd(scores))
print(make_list(6))