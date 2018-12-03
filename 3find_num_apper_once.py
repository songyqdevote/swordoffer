
def FindNumsAppearOnce(self, array):
    tmp = []
    for i in array:
        if i in tmp:
            tmp.remove(i)
        else:
            tmp.append(i)
    return tmp