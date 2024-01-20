object Solution {
    def isValid(s: String): Boolean = {
        val closeToOpen = Map(')' -> '(', ']' -> '[', '}' -> '{')

        def loop(idx: Int = 0, acc: List[Char] = Nil): Boolean = (idx, acc) match {
            case (idx, Nil) if idx == s.length => true
            case (idx, acc) if idx == s.length => false
            case (idx, head :: tail) if closeToOpen.contains(s(idx)) && closeToOpen(s(idx)) == head => loop(idx + 1, tail)
            case (idx, acc) if !closeToOpen.contains(s(idx)) => loop(idx + 1, s(idx) :: acc)
            case _ => false
        }
        
        loop()
    }
}