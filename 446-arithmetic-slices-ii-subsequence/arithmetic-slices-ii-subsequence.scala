import scala.collection.mutable.HashMap

object Solution {
    def numberOfArithmeticSlices(nums: Array[Int]): Int = {
        var res = 0
        val dp = Array.fill(nums.length)(HashMap[Long, Int]())

        for {i <- 0 until nums.length
            j <- 0 until i} {
                val diff = nums(i).toLong - nums(j)
                dp(i).update(diff, dp(i).getOrElse(diff, 0) + 1)
                res += 1
                if (dp(j).contains(diff)) {
                    res += dp(j)(diff)
                    dp(i).update(diff, dp(j)(diff) + dp(i)(diff))
                }
            }

        res - (nums.length * (nums.length - 1) / 2)
    }
}