import scala.annotation._

object Solution {
    def rob(nums: Array[Int]): Int = {
        @tailrec
        def loop(idx: Int = 0, twoBack: Int = 0, oneBack: Int = 0): Int = {
            if (idx == nums.length) oneBack
            else loop(idx + 1, oneBack, math.max(oneBack, twoBack + nums(idx)))
        }

        loop()
    }
}