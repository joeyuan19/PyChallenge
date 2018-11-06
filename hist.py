class Histogram(dict):
    def __init__(self,li):
        for i in li:
            if i not in self:
                self[i] = 1
            else:
                self[i] += 1
