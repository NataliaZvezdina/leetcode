import scala.collection.immutable._

object Solution {
    def isAnagram(s: String, t: String): Boolean = {
        if (s.length != t.length) false

        s.groupMapReduce(identity)(_ => 1)(_ + _) == t.groupMapReduce(identity)(_ => 1)(_ + _)
    }
}