/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def rangeSumBST(root: TreeNode, low: Int, high: Int): Int = {
        
        def loop(tr: List[TreeNode], acc: Int = 0): Int = {
            tr.headOption match {
                case None => acc
                case Some(head) if head.value < low => loop(Option(head.right).toList ::: tr.tail,  acc)
                case Some(head) if head.value > high => loop(Option(head.left).toList ::: tr.tail,  acc)
                case Some(head) => loop(List(head.left, head.right).flatMap(Option(_)) ::: tr.tail, acc + head.value)
            }
        }

        loop(Option(root).toList)
    }
}