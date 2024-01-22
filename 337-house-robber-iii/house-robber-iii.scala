/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */

object Solution {
    def rob(root: TreeNode): Int = {
        def dfs(node: TreeNode): (Int, Int) = Option(node) match {
            case None => (0, 0)
            case Some(node) => {
                val (withRootLeft, withoutRootLeft) = dfs(node.left)
                val (withRootRight, withoutRootRight) = dfs(node.right)
                (node.value + withoutRootLeft + withoutRootRight, math.max(withRootLeft, withoutRootLeft) + math.max(withRootRight, withoutRootRight))
            }
        }

        val (withRoot, withoutRoot) = dfs(root)

        math.max(withRoot, withoutRoot)
    }
}