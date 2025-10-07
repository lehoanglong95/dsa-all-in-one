"""
Link: https://leetcode.com/problems/camelcase-matching/

Description:
Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true if queries[i] matches pattern, and false otherwise.

A query word queries[i] matches pattern if you can insert lowercase English letters into the pattern so that it equals the query. You may insert a character at any position in pattern or you may choose not to insert any characters at all.

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 

Constraints:

1 <= pattern.length, queries.length <= 100
1 <= queries[i].length <= 100
queries[i] and pattern consist of English letters.

"""

class Node:

    def __init__(self):
        self.child = dict()
        self.val = ""

class Trie:

    def __init__(self):
        self.root = Node()
    
    def add(self, query):
        temp_root = self.root
        for ch in query:
            if ch not in temp_root.child:
                temp_root.child[ch] = Node()
            temp_root = temp_root.child[ch]
        temp_root.val = query
    
    def search(self, root, pattern, idx):
        if idx == len(pattern) and root.val:
            return [root.val]
        ans = []
        if idx == len(pattern):
            for key, node in root.child.items():
                if key.islower():
                    ans.extend(self.search(node, pattern, idx))
        else:
            ch = pattern[idx]
            for key, node in root.child.items():
                if key.islower():
                    if key == ch:
                        ans.extend(self.search(node, pattern, idx + 1))
                    else:
                        ans.extend(self.search(node, pattern, idx))
                else:
                    if key == ch:
                        ans.extend(self.search(node, pattern, idx + 1))
        return ans


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie = Trie()
        for query in queries:
            trie.add(query)
        
        valid_queries = set(trie.search(trie.root, pattern, 0))
        return [query in valid_queries for query in queries]
            