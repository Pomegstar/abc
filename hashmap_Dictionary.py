#problem 1: "how many nums are smaller than current nums"
class solution_hashmap: 
  def c(self, nums: list[int]):
         dic = {}
         ans = []
         sorted_list = sorted(nums)
         for i in range(len(sorted_list)):
            if sorted_list[i] not in dic:
                   dic[sorted_list[i]] = i
         for num in nums:
                ans.append(dic[num])
         return ans
z = solution_hashmap(3,4,5,6)
#=========================================================================================================
#problem 2: 2 sum
dic2 = {}
list = [7,3,2,6]
target = 9
ans = []
for i in range(len(list)):
 for j in range(len(list)):
    if list[i] + list[j] == target:
      dic2[list[i]] = i
for x in list:
    if x in dic2:
        ans.append(dic2[x])
if ans == []:
    print("not found")   
print(ans)
    