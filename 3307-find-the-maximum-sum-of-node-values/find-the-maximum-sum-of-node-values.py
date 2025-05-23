class Solution:
    def maximumValueSum(self, nums, k, edges):
        n = len(nums)
        deltas = []
        total_sum = sum(nums)

        for num in nums:
            flipped = num ^ k
            delta = flipped - num
            deltas.append(delta)

        deltas.sort(reverse=True)

        max_sum = total_sum
        current_sum = total_sum

        for i in range(0, n, 2):
            if i + 1 >= n:
                break
            if deltas[i] + deltas[i + 1] <= 0:
                break
            current_sum += deltas[i] + deltas[i + 1]
            max_sum = max(max_sum, current_sum)

        return max_sum

# Example driver code
param_1 = [1, 2, 3]
param_2 = 4
param_3 = [[0, 1], [1, 2]]

ret = Solution().maximumValueSum(param_1, param_2, param_3)
print(ret)  # Output: 11
