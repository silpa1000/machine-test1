def solution(nums,target):
  dic={}
  for i in range(len(nums)):
    dic[nums[i]]=i
  for i in range(len(nums)):
    y=target-nums[i]
    if y in dic:
      return[i,dic[y]]
print(solution([1,3,6,9],4))