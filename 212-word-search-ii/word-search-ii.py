class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.count = 0
    
    def addWord(self, word):
        cur = self
        cur.count += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
            cur.count += 1
        cur.isWord = True
    
    def removeWord(self, word):
        cur = self
        cur.count -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.count -= 1
        cur.isWord = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        root = Trie()
        for word in words:
            root.addWord(word)
        res = set()
        visit = set()
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children or node.children[board[r][c]].count < 1:
                return False
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                node.isWord = False
                root.removeWord(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)