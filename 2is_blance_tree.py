# _*_ coding utf-8

class TreeNode:
    def __init__(self,x):
        self.value = x
        self.left = None
        self.righr = None


def TreeDepth(self, pRoot):
    if pRoot is None:
        return 0
    return (1 + max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)))


def IsBalanced_Solution(self, pRoot):
    if pRoot is None:
        return True
    if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
        return False
    return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
