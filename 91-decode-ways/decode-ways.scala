object Solution {
    def numDecodings(s: String): Int = {
        if (s == null || s.length == 0) return 0
        val memo = scala.collection.mutable.Map[Int, Int]()

        def dfs(idx: Int): Int = idx match {
            case i if i == s.length => 1
            case i if s(i) == '0' => 0
            case i if i == s.length - 1 => 1
            case i if memo.contains(i) => memo(i)
            case i => {
                var ans = dfs(i+1)
                if (s.substring(i, i+2).toInt <= 26) {
                    ans += dfs(i+2)
                }
                memo.put(i, ans)
                ans
            }
        }

        dfs(0)
    }
}
