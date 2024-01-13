import scala.collection.mutable.Map

object Solution {
    def minSteps(s: String, t: String): Int = {
        val mp = Map.empty[Char, Int].withDefaultValue(0)
        for (i <- 0 until s.length) {
            mp(s(i)) += 1
            mp(t(i)) -= 1
        }

        mp.values.filter(n => n > 0).sum
    }
}