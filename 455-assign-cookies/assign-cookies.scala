import scala.util.control.Breaks._

object Solution {
    def findContentChildren(g: Array[Int], s: Array[Int]): Int = {
        val gSorted = g.sorted
        val sSorted = s.sorted
        var i, j = 0
        
        breakable {
            while (i < gSorted.length) {
                while (j < sSorted.length && gSorted(i) > sSorted(j)) {
                    j += 1
                }
                if (j < sSorted.length) {
                    i += 1
                    j += 1
                } else {
                    break
                }
            }
        }
        i
    }
}