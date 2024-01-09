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
    def leafSimilar(root1: TreeNode, root2: TreeNode): Boolean = {

        def dfs(root: TreeNode, leafs: List[Int]): TailRec[List[Int]] = Option(root) match {
            case None => done(List[Int]())
            case Some(root) if root.left == null && root.right == null => done(List(root.value))
            case _ => for {
                l <- dfs(root.left, leafs)
                r <- dfs(root.right, leafs)
            } yield l ::: r
        }

        dfs(root1, List[Int]()).result == dfs(root2, List[Int]()).result
    }

}