import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def makePost(preStart, preEnd, inStart, inEnd):
    if (preStart > preEnd) or (inStart > inEnd):
        return
    root = preorder[preStart]    #preorder의 시작 노드가 루트
    rootIndex = nodeIndex[root]  #inorder에서 root의 index
    leftCount = rootIndex - inStart #왼쪽 서브트리 노드의 개수
    rightCount = inEnd - rootIndex  #오른쪽 서브트리 노드의 개수

    makePost(preStart + 1, preStart + leftCount, inStart, inStart + leftCount - 1)  #왼쪽 서브트리에 대해 탐색
    makePost(preEnd - rightCount + 1, preEnd, inEnd - rightCount + 1, inEnd)    #오른쪽 서브트리에 대해 탐색
    print(root)

T = int(input())
for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    nodeIndex = [0 for _ in range(n + 1)]
    for i in range(0,n):
        nodeIndex[inorder[i]]=i
    makePost(0,n-1,0,n-1)


