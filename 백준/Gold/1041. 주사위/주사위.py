n = int(input())
s = list(map(int,input().split()))

nums = []

result = 0

if n == 1:
    print(sum(s)-max(s))
else:
    nums.append(min(s[0], s[5]))
    nums.append(min(s[1], s[4]))
    nums.append(min(s[2], s[3]))

    nums.sort()

    n3 = 4
    n2 = (n-2)*4 + (n-1)*4
    n1 = (n-2)*(n-2) + (n-1)*(n-2)*4

    result = n1 * nums[0] + n2 * (nums[0]+nums[1]) + n3 * sum(nums)

    print(result)