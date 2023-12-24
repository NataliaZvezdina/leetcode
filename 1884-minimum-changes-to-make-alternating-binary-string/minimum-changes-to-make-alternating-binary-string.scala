object Solution {
    def minOperations(s: String): Int = {
        val cnt = s.zipWithIndex.count {
            case (c, i) => i % 2 == 0 && c == '1' || i % 2 == 1 && c == '0'
        }

        Math.min(cnt, s.length - cnt)
    }
}
