import sys
input = sys.stdin.readline

stack = []
size = 0

n = int(input())
for _ in range(n):
    commandList = list(input().split())
    command = commandList[0]
    if command == 'push':
        stack.append(commandList[1])
        size+=1
    elif command == 'pop':
        if size>0:
            print(stack.pop())
            size-=1
        else:
            print(-1)
    elif command == 'size':
        print(size)
    elif command == 'empty':
        if size==0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if size>0:
            print(stack[-1])
        else:
            print(-1)

