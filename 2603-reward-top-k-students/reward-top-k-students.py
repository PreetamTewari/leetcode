from heapq import *
class Solution:
    def topStudents(self, pf: List[str], nf: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos = set(pf)
        neg = set(nf)
        heap= []
        for i in range(len(student_id)):
            c = 0
            b = "".join(report[i]).split(" ")
            for j in b:
                if j in pos:
                    c += 3
                elif j in neg:
                    c -= 1
            heappush(heap,[-c, student_id[i]])
        res = []
        while k:
            l = heappop(heap)
            res.append(l[1])
            k-=1
        return res