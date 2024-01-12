/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */

object Solution {
    def postorderTraversal(root: TreeNode): List[Int] = {
        
        @scala.annotation.tailrec
        def dfs(lst: List[TreeNode], acc: List[Int]): List[Int] = lst match {
            case Nil => acc
            case null :: tail => dfs(tail, acc)
            case node :: tail => dfs(node.right :: node.left :: tail, node.value :: acc)
        }

        dfs(List(root), Nil)
    }
}