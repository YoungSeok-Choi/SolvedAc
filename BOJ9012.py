
def main():

    iterNum = int(input())

    for i in range(iterNum):
        tempStr = input()
        flag = True
        stack = []

        for j in tempStr:
            
            if j == "(":
                stack.append(j)
            else:
                if len(stack) == 0 or stack[-1] != "(":
                    flag = False
                    break
                else: 
                    stack.pop()    

        if len(stack) == 0 and flag:
            print("YES")
        else:
            print("NO")

            
if __name__ == "__main__":
    main()



