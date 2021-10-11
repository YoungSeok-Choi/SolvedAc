import sys
sys.setrecursionlimit(100000)

# 2583 
# call by value Tlqkf Tlqkf....

def dfs(i, j, area, dfs_map):

    if i < 0 or i >= len(dfs_map) or \
        j < 0 or j >= len(dfs_map[0]) or \
        dfs_map[i][j] == False:
        return

    #visited 
    dfs_map[i][j] = False

    area[0] += 1

    dfs(i+1, j, area, dfs_map)
    dfs(i-1, j, area, dfs_map)
    dfs(i, j+1, area, dfs_map)
    dfs(i, j-1, area, dfs_map)

#input
M, N, K = map(int, input().split())
points = []

#output
counts = 0
answ = []

#2차원 배열 입력 
for _ in range(K):
    points.append(list(map(int, input().split())))

# 머릿속으로는 초기화 하는 동시에 조건문으로 순환을 돌아야 할 T/F 나뉘는 2D배열을 초기화시키고 싶다.
dfs_map = [[True for _ in range(N)] for _ in range(M)]

#후보군 줄이기..? O(n^3)
for k in range(K):
    for i in range(M):
        for j in range(N):
            if (i >= points[k][1] and i+1 <= points[k][3]) and \
                (j >= points[k][0] and j+1 <= points[k][2]): 
                dfs_map[i][j] = False

for i in range(M):
    for j in range(N):
        if dfs_map[i][j] == True:
            area = [0]
            counts += 1 
            dfs(i, j, area, dfs_map)
            answ.append(area[0])

answ.sort()

print(counts)

for i in answ:
    print("{0} ".format(i), end='')


# 파일 입출력 ver.
# with open("./input.txt", "r") as f:

#     M, N, K = map(int, f.readline().split())
#     #2차원 배열 입력 
#     for _ in range(K):
#         points.append(list(map(int, f.readline().split())))


#     # 머릿속으로는 초기화 하는 동시에 조건문으로 순환을 돌아야 할 0/1 나뉘는 배열을 초기화시키고 싶다.
#     dfs_map = [[True for _ in range(N)] for _ in range(M)]

#     #후보군 줄이기..? n^3 홀리 쓍\ㅅ
#     for k in range(K):
#         for i in range(M):
#             for j in range(N):
#                 if (i >= points[k][1] and i+1 <= points[k][3]) and \
#                     (j >= points[k][0] and j+1 <= points[k][2]): 
#                     dfs_map[i][j] = False

#     for i in range(M):
#         for j in range(N):
#             if dfs_map[i][j] == True:
#                 area = [0]
#                 counts += 1 
#                 dfs(i, j, area, dfs_map)
#                 answ.append(area[0])

#     answ.sort()

#     print(counts)

#     for i in answ:
#         print("{0} ".format(i), end='')



#input
# M, N, K = map(int, input().split())
# for _ in range(K):
# points.append(list(map(int, input().split())))