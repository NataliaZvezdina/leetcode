import scala.collection.mutable.Map

object Solution {
    def containsDuplicate(nums: Array[Int]): Boolean = {
        val mp = Map.empty[Int, Int].withDefaultValue(0)
        for (num <- nums) mp(num) += 1

        mp.exists{ case (_, v) => v > 1 }
    }
}