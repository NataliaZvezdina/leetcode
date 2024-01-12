/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def inorderTraversal(root: TreeNode): List[Int] = {
        val res = scala.collection.mutable.ListBuffer[Int]()

        def dfs(node: TreeNode): Unit = Option(node) match {
            case None =>
            case Some(node) => {
                dfs(node.left)
                res.addOne(node.value)
                dfs(node.right)
            }
        }

        dfs(root)
        res.toList
    }
}