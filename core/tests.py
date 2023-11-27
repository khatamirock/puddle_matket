# from django.test import TestCase

# Create your tests here.

nums=[2,4,6,8]
n=len(nums)
prefix_sum = [0] * n
suffix_sum = [0] * n

# Calculate prefix sums
prefix_sum[0] = nums[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]


print(prefix_sum)