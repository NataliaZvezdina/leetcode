object Solution {
    def makeEqual(words: Array[String]): Boolean = {
        words.mkString
             .groupBy(identity)
             .mapValues(_.size)
             .forall(n => n._2 % words.size == 0)
    }
}