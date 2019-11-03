s = list(input())

now = '>'
count = 0
nums = []
score = 0

for i in range(len(s)) :
    if s[i] == now :
        count += 1
    else :
        nums.append(count)
        count = 1
        now = s[i]

nums.append(count)

if s[len(s) - 1] == '>' :
    nums.append(0)

for j in range(len(nums)) :
    score += nums[j] * (nums[j] + 1) //2
    if j > 0 and j % 2 == 0 :
        if nums[j - 1] > nums[j] :
            score -= nums[j]
        else :
            score -= nums[j - 1]

print(score)