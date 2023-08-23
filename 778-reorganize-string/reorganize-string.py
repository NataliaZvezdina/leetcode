class Solution:
    def reorganizeString(self, s: str) -> str:

        cnt = Counter(s)
        heap = [[-count, char] for char,count in cnt.items()]
        heapq.heapify(heap)

        prev = None
        res = ''
        while heap or prev:
            if prev and not heap:
                return ''

            count, char = heapq.heappop(heap)
            res += char
            count += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if count < 0:
                prev = [count, char]

        return res
