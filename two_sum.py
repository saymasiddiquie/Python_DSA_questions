nums = list(map(int, input().split()))
target = int(input())

d = {}

for i in range(len(nums)):
    complement = target - nums[i]
    
    if complement in d:
        for index in d[complement]:
            print(index, i)
    if nums[i]  in d:
        d[nums[i]].append(i)
    else:
        d[nums[i]] = [i]
