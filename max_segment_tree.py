class SegTree:
    def __init__(self, baskets):
        self.n = len(baskets)
        size = 2 << (self.n - 1).bit_length()
        self.seg = [0] * size
        self._build(baskets, 0, 0, self.n - 1)

    def _maintain(self, o):
        self.seg[o] = max(self.seg[o * 2 + 1], self.seg[o * 2 + 2])

    def _build(self, a, o, l, r):
        if l == r:
            self.seg[o] = a[l]
            return
        m = (l + r) // 2
        self._build(a, o * 2 + 1, l, m)
        self._build(a, o * 2 + 2, m + 1, r)
        self._maintain(o)

    def find_first_and_update(self, o, l, r, x):
        print(f"node: {o}, left: {l}, right: {r}, x: {x}")
        if self.seg[o] < x:
            return False
        if l == r:
            self.seg[o] = -1
            return True
        m = (l + r) // 2
        is_find = self.find_first_and_update(o * 2 + 1, l, m, x)
        if not is_find:
            is_find = self.find_first_and_update(o * 2 + 2, m + 1, r, x)
        self._maintain(o)
        return is_find


baskets = [3, 5, 4]
fruits = [4, 2, 5]

m = len(baskets)

tree = SegTree(baskets)
count = 0
print(tree.seg)
for fruit in fruits:
    tree.find_first_and_update(0, 0, 2, fruit)
    print(tree.seg)

