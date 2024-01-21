import scala.annotation._

object Solution {
    def rob(nums: Array[Int]): Int = {
        @tailrec
        def loop(idx: Int, prev: Int, curr: Int): Int = {
            if (idx == nums.length) curr
            else loop(idx + 1, curr, math.max(curr, prev + nums(idx)))
        }

        if (nums.length == 1) nums(0)
        else loop(2, nums(0), math.max(nums(0), nums(1)))
    }
}