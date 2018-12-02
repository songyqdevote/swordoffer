# _*_ coding:utf-8 _*_


class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def TreeDepth(self, pRoot):
    if pRoot == None:
        return 0
    return 1 + max(TreeDepth(pRoot.left), TreeDepth(pRoot.right))
