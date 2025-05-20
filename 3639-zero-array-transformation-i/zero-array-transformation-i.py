class Solution:
    def isZeroArray(self, nums, queries):
        n = len(nums)
        count = [0] * (n + 1)

        # Apply range increments
        for l, r in queries:
            count[l] += 1
            if r + 1 < n:
                count[r + 1] -= 1

        # Build prefix sum to get number of times each index is covered
        times = [0] * n
        times[0] = count[0]
        for i in range(1, n):
            times[i] = times[i - 1] + count[i]

        # Check if each number can be reduced to 0
        for i in range(n):
            if nums[i] > times[i]:
                return False

        return True
