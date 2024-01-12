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
    def inorderTraversal(root: TreeNode): List[Int] = {
        
        def dfs(node: TreeNode, lst: List[Int]): TailRec[List[Int]] = Option(node) match {
            case None => done(List.empty)
            case Some(node) =>
                for {
                    l <- dfs(node.left, lst)
                    r <- dfs(node.right, lst)
                } yield l ::: List(node.value) ::: r
        }        

        dfs(root, List.empty[Int]).result
    }
}