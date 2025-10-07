class UF:

    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        par_x = self.find(x)
        par_y = self.find(y)
        if par_x == par_y:
            return
        self.parents[par_x] = par_y