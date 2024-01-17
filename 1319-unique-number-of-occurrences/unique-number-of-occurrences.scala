import scala.collection.mutable.Map

object Solution {
    def uniqueOccurrences(arr: Array[Int]): Boolean = {
        val mp = Map.empty[Int, Int].withDefaultValue(0)
        for (num <- arr) mp(num) += 1
        val fq = mp.values.toSeq

        def loop(fq: Seq[Int], acc: Set[Int] = Set[Int]()): Boolean = fq match {
            case Nil => true
            case head :: tail if acc.contains(head) => false
            case head :: tail => loop(tail, acc + head)
        }

        loop(fq)
    }
}