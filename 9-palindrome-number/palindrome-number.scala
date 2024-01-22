import scala.annotation.tailrec

object Solution {
    def isPalindrome(x: Int): Boolean = {
        val aString = x.toString

        @tailrec
        def loop(left: Int, right: Int): Boolean = {
            if (left >= right) true
            else if (aString(left) != aString(right)) false
            else loop(left + 1, right - 1)
        }

        loop(0, aString.length - 1)
    }
}