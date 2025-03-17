
from collections import deque


def minimumPlatform(arr,dep):
        arr.sort()
        dep.sort()
        i = 0
        j = 0
        platform_count = 0
        max_platform = 0
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                platform_count += 1
                i += 1
            else: 
                #arr[i] > dep[j]:
                platform_count -= 1
                j += 1
            max_platform = max(max_platform, platform_count)
        return max_platform
            



        

if __name__ == "__main__":

    arr = [2225, 1729, 1835, 951, 1143, 515, 1525, 743, 1025, 1611, 1827, 2203, 1116, 1514, 723]
    dep = [2231, 2003, 2149, 2252, 2352, 2153, 1625, 1049, 1337, 1639, 2151, 2330, 1633, 1611, 2009]
    
    print(minimumPlatform(arr, dep))
