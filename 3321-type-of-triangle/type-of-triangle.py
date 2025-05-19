class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Sort the sides to easily apply the triangle inequality
        a, b, c = sorted(nums)

        # Check if the sides can form a triangle
        if a + b <= c:
            return "none"
        
        # Determine the type of the triangle
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"


# Example usage:
sol = Solution()
print(sol.triangleType([3, 3, 3]))  # Output: equilateral
print(sol.triangleType([3, 4, 5]))  # Output: scalene
print(sol.triangleType([3, 3, 5]))  # Output: isosceles
print(sol.triangleType([1, 2, 3]))  # Output: none
        