import sys
sys.setrecursionlimit(100000)


def DFS(array_2d, N, i, j, k, visited):

    # 행렬의 벽 밖으로 나가는 경우 + 벽 안에 위치하지만, 이미 방문한 영역이거나 빗물에 잠긴 영역인 경우
    if i < 0 or i >= N or \
        j < 0 or j >= N or \
        array_2d[i][j] <= k or visited[i][j] == 0: return
    
    visited[i][j] = 0

    # 상 하 좌 우 
    DFS(array_2d, N, i+1, j, k, visited)
    DFS(array_2d, N, i-1, j, k, visited)
    DFS(array_2d, N, i, j+1, k, visited)
    DFS(array_2d, N, i, j-1, k, visited)


array_2d = []
safeAreaSet = []
visited = []

maxOfArray = 0

N = int(sys.stdin.readline())
for i in range(N):
    array_2d.append(list(map(int,sys.stdin.readline().split())))

#2차원배열의 최대값 찾기
for row in array_2d:
    if maxOfArray < max(row):
        maxOfArray = max(row)

#빗물 높이 0 ~ maxOfArray-1 경우에서 각각의 높이별 안전영역 구하기 + 최대값 찾기
for k in range(maxOfArray):

    safeArea = 0
    visited = [[1 for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            if array_2d[i][j] > k and visited[i][j] == 1:
                safeArea += 1;
                DFS(array_2d, N, i, j, k, visited)

    safeAreaSet.append(safeArea)

print(max(safeAreaSet))