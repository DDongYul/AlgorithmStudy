#후위의 맨 끝 노드가 루트, 루트 기준으로 중위에서 왼쪽 오른쪽 나눔, 나눈 서브트리의 개수만큼 후위에서 나누고 이떄 끝이 다시 루트 -> 재귀 이용
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def preorder(inStart,inEnd,postStart,postEnd):
    if (inStart > inEnd) or (postStart > postEnd):
        return
    root = postorder[postEnd]
    print(root)
    left = nodeNum[root]-inStart
    right = inEnd - nodeNum(root)

    preorder(inStart, inStart + left - 1, postStart, postStart + left - 1)
    preorder(inEnd - right + 1, inEnd, postEnd - right, postEnd - 1)

n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
nodeNum = [0] * (n + 1)
for i in range(n):
    nodeNum[inorder[i]] = i
preorder(0,n-1,0,n-1)



