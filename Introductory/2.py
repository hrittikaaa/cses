n = int(input())
t_sum = (n*(n+1)) // 2
nums = input().split()
nums = [int(i) for i in nums]

print(t_sum-sum(nums))