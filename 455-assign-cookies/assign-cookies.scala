import scala.annotation.tailrec

object Solution {
    def findContentChildren(g: Array[Int], s: Array[Int]): Int = {
        val gSorted = g.sorted
        val sSorted = s.sorted
        
        @tailrec
        def run(gIdx: Int = 0, sIdx: Int = 0, acc: Int = 0): Int = {
            if (gIdx >= gSorted.size || sIdx >= sSorted.size) acc
            else if (gSorted(gIdx) <= sSorted(sIdx)) run(gIdx+1, sIdx+1, acc+1)
            else run(gIdx, sIdx+1, acc)
        }

        run()
    }
}