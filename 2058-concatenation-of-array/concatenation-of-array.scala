object Solution {
    def getConcatenation(nums: Array[Int]): Array[Int] = {
        val ar: Array[Int] = Array.ofDim(2 * nums.length)
        for (idx <- 0 until nums.length) {
            ar(idx) = nums(idx)
            ar(idx + nums.length) = nums(idx)
        }
        ar
    }
}