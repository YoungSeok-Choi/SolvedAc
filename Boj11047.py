import math
# 11047
N, K = map(int, input().split())
kindsOfCoins = []

for _ in range(N):
    temp = int(input())
    kindsOfCoins.append(temp)

numOfCoins = 0
while K != 0:
    
    for i in range(len(kindsOfCoins)):
        if K / int(kindsOfCoins[len(kindsOfCoins) - (i+1)]) == 0:
            continue
        else:
            numOfCoins += math.floor(K / int(kindsOfCoins[len(kindsOfCoins) - (i+1)]))
            K %= int(kindsOfCoins[len(kindsOfCoins) - (i+1)])

print(numOfCoins)


# with open("./input.txt", "r") as f:

# N, K = map(int, f.readline().split())

# for _ in range(N):
#     temp = f.readline()
#     kindsOfCoins.append(temp)

# numOfCoins = 0
# while K != 0:
    
#     for i in range(len(kindsOfCoins)):
#         if K / int(kindsOfCoins[len(kindsOfCoins) - (i+1)]) == 0:
#             continue
#         else:
#             numOfCoins += math.floor(K / int(kindsOfCoins[len(kindsOfCoins) - (i+1)]))
#             K %= int(kindsOfCoins[len(kindsOfCoins) - (i+1)])

# print(numOfCoins)