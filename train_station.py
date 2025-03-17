
from collections import deque


def minimumPlatform(arr,dep):
    train_list = []
    for i in range(len(arr)):
        train = [arr[i], dep[i]]
        train_list.append(train)
    train_list.sort(key=lambda x: x[0])
    #print(train_list)
    max_platform = 0
    platform_count = 0
    trains_on_platform = [False] * len(arr)
    for i in range(len(train_list)):
        for j in range(len(trains_on_platform)):
            if trains_on_platform[j] == True:
                if train_list[j][1] < train_list[i][0]:
                    trains_on_platform[j] = False
        trains_on_platform[i] = True
        platform_count = 0
        for b in trains_on_platform:
            if b == True:
                platform_count += 1
        max_platform = max(max_platform, platform_count)
        #print(f"trains_on_platform: {platform_count: }{trains_on_platform}")
    return max_platform
        

if __name__ == "__main__":

    arr = [2225, 1729, 1835, 951, 1143, 515, 1525, 743, 1025, 1611, 1827, 2203, 1116, 1514, 723]
    dep = [2231, 2003, 2149, 2252, 2352, 2153, 1625, 1049, 1337, 1639, 2151, 2330, 1633, 1611, 2009]
    
    print(minimumPlatform(arr, dep))
