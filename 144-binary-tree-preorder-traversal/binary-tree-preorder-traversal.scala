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
    def preorderTraversal(root: TreeNode): List[Int] = {
        
        def dfs(node:TreeNode, lst: List[Int]): TailRec[List[Int]] = Option(node) match {
            case None => done(Nil)
            case Some(node) => {
                for {
                    l <- dfs(node.left, lst)
                    r <- dfs(node.right, lst)
                } yield List(node.value) ::: l ::: r
            }
        }

        dfs(root, List[Int]()).result
    }
}