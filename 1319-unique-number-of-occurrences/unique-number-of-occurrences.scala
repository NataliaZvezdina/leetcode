import scala.collection.mutable.Map

object Solution {
    def uniqueOccurrences(arr: Array[Int]): Boolean = {
        val mp = Map.empty[Int, Int].withDefaultValue(0)
        for (num <- arr) mp(num) += 1
        mp.values.forall(fq => mp.values.count(fqCount => fq == fqCount) == 1)
    }
}