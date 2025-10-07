class SegmentTree:
    """0-indexed segment tree implementation"""
    
    def __init__(self, arr):
        """
        Initialize segment tree with given array.
        Time complexity: O(n)
        Space complexity: O(4n) = O(n)
        """
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Tree array
        self.build(arr, 0, 0, self.n - 1)  # Start from node 0
    
    def build(self, arr, node, start, end):
        """
        Build the segment tree recursively.
        node: current node index in tree (0-indexed)
        start, end: range [start, end] that current node represents
        """
        if start == end:
            # Leaf node - store array element
            self.tree[node] = arr[start]
        else:
            # Internal node - recursively build left and right subtrees
            mid = (start + end) // 2
            left_child = 2 * node + 1   # 0-indexed: left child formula
            right_child = 2 * node + 2  # 0-indexed: right child formula
            
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            
            # Internal node value = sum of children
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def update(self, idx, val):
        """
        Update element at index idx to value val.
        Time complexity: O(log n)
        """
        self._update(0, 0, self.n - 1, idx, val)
    
    def _update(self, node, start, end, idx, val):
        """Helper function for update operation."""
        if start == end:
            # Leaf node - update value
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1   # 0-indexed navigation
            right_child = 2 * node + 2  # 0-indexed navigation
            
            if idx <= mid:
                # Update left subtree
                self._update(left_child, start, mid, idx, val)
            else:
                # Update right subtree
                self._update(right_child, mid + 1, end, idx, val)
            
            # Update current node after children are updated
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query(self, l, r):
        """
        Query sum in range [l, r] (inclusive).
        Time complexity: O(log n)
        """
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        """Helper function for range query."""
        # No overlap
        if r < start or end < l:
            return 0
        
        # Complete overlap - current segment is completely within query range
        if l <= start and end <= r:
            return self.tree[node]
        
        # Partial overlap - recurse on children
        mid = (start + end) // 2
        left_child = 2 * node + 1   # 0-indexed navigation
        right_child = 2 * node + 2  # 0-indexed navigation
        
        left_sum = self._query(left_child, start, mid, l, r)
        right_sum = self._query(right_child, mid + 1, end, l, r)
        
        return left_sum + right_sum