/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */

import scala.collection.mutable.Map
import scala.collection.mutable.Set

object Solution {
    def amountOfTime(root: TreeNode, start: Int): Int = {
        
        val graph = Map.empty[Int, List[Int]].withDefaultValue(List[Int]())
        def dfs(root: TreeNode): Unit = {
            if (root != null) {
                if (root.left != null) {
                    graph(root.value) ::= root.left.value
                    graph(root.left.value) ::= root.value
                    dfs(root.left)
                }
                if (root.right != null) {
                    graph(root.value) ::= root.right.value
                    graph(root.right.value) ::= root.value
                    dfs(root.right)
                }
            }
            
            
        }

        dfs(root)

        val visited = Set(start)
        var minutes = -1
        var q = List(start)
        while (q.nonEmpty) {
            q = q.flatMap(graph(_)).filter(visited.add(_))
            minutes += 1
        }

        minutes
    }
}