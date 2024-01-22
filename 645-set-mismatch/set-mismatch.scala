object Solution {
    def findErrorNums(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        val st = nums.toSet
        val missing = (1 to n).find(!st.contains(_)).get
        val duplicate = nums.sum - n * (n + 1) / 2 + missing

        Array(duplicate, missing)
    }
}