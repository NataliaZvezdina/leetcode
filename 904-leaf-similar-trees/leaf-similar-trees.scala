/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def leafSimilar(root1: TreeNode, root2: TreeNode): Boolean = {
        
        def dfs(root: TreeNode): List[Int] = Option(root) match {
            case None => List[Int]()
            case Some(root) if root.left == null && root.right == null => List(root.value)
            case _ => dfs(root.left) ::: dfs(root.right)
        }

        dfs(root1) == dfs(root2)
    }
}