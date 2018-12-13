# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        cols = len(array[0])
        i = 0
        j = cols - 1
        while j >= 0 and i < rows:
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                j = j - 1
            else:
                i = i + 1
        return False