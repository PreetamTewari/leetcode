class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pat = word[:j] + '*' + word[j+1:]
                nei[pat].append(word)

        q = deque([beginWord])
        visit = set([beginWord])
        res = 1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pat = word[:j] + '*' + word[j+1:]
                    for neiWord in nei[pat]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0