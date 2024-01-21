import scala.annotation._

object Solution {
    def rob(nums: Array[Int]): Int = {        
        @tailrec
        def loop(idx: Int, len: Int, twoBack: Int = 0, oneBack: Int = 0): Int = {
            if (len == 0) oneBack
            else loop(idx + 1, len - 1, oneBack, math.max(twoBack + nums(idx), oneBack)) 
        }

        if (nums.length == 1) nums(0)
        else math.max(loop(0, nums.length - 1), loop(1, nums.length - 1))
    }
}