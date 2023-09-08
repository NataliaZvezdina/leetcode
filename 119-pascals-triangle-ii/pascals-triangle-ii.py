class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        for i in range(rowIndex):
            tmp = [0] + prev + [0]
            row = []
            for j in range(len(tmp)-1):
                row.append(tmp[j] + tmp[j+1])
            prev = row

        return prev
        