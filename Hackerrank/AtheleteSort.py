
n_m = list(map(int, input().split()))

table = list()

for i in range(n_m[0]):
    table.append(list(map(int, input().split())))
    
k = int(input())

sorted_table = sorted(table, key=lambda record: record[k])

for item in sorted_table:
    print(*item)


# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1