if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print (sorted(set(arr))[-2])

#     5
# 2 3 6 6 5