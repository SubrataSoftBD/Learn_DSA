from typing import List

def linear_search(dataList: List, target: int):
    size = len(dataList)
    for index in range(0, size):
        if(dataList[index] == target):
            return index
    return "No data found"


my_list = [1,55, 12, 11, 25, 58, 50]
target = 500

print(linear_search(my_list, target))