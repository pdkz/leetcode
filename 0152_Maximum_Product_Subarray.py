class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = nums[0]
        min_product = nums[0]
        max_product = nums[0]

        N = len(nums)
        for i in range(1,N):
            if nums[i] > 0:
                max_product = max(nums[i], max_product*nums[i])
                min_product = min(nums[i], min_product*nums[i])
            else:
                max_product_tmp = max(nums[i], min_product*nums[i])
                min_product = min(nums[i], max_product*nums[i])
                max_product = max_product_tmp

            result = max(result, max_product)

        return result
