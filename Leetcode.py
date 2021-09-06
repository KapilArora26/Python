# Problem of 2 sums

def getindices(nums, prev, curr):
    pos = '['
    if prev == curr:
        valueatfirstpos = nums.index(prev)
        valueatsecondpos = nums.index(prev,valueatfirstpos+1)
        pos = pos + str(valueatfirstpos) + ',' + str(valueatsecondpos) + ']'

    else:
        pos = pos + str(nums.index(prev)) + ',' + str(nums.index(curr)) + ']'
    return pos

nums = input()
target = input()
nums = nums.replace('[','')
nums = nums.replace(']','')

nums = nums.split(',')

prev = 0

for temp in nums:
    if int(prev)+int(temp) == int(target):
         print(getindices(nums, prev, temp))
         break
    else:
        prev = temp
