import scala.annotation.tailrec
import scala.collection.mutable.ListBuffer

object Solution {
    def findMatrix(nums: Array[Int]): List[List[Int]] = {
        val mp = nums.groupBy(identity)
                     .view
                     .mapValues(_.length)
                     .toMap

        @tailrec
        def loop(mp: Map[Int, Int], res: ListBuffer[List[Int]]): ListBuffer[List[Int]] = {
            if (mp.isEmpty) res
            else {
                val row = mp.keys.toList
                val freshMp = mp.view
                                .mapValues(_ - 1)
                                .filter{case (_, freq) => freq > 0}
                                .toMap
                loop(freshMp, res += row)
            }
        }
        
        loop(mp, res = new ListBuffer[List[Int]]).toList
    }
}