/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */

import scala.util.control.TailCalls._

object Solution {
    def rangeSumBST(root: TreeNode, low: Int, high: Int): Int = {

        def dfs(root: TreeNode, acc: Int = 0): TailRec[Int] = Option(root) match {
            case None => done(0)
            case Some(root) if root.value < low => dfs(root.right, acc)
            case Some(root) if root.value > high => dfs(root.left, acc)
            case _ => for (
                l <- dfs(root.left, acc);
                r <- dfs(root.right, acc)
            ) yield l + r + root.value
        }

        dfs(root).result

    }
}