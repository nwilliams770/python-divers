class Solution:
  def singleNumber(self, nums: List[int]) -> int:
      counter_map = dict()
      for num in nums:
          counter_map[num] = counter_map.get(num, 0) + 1
      for key in counter_map:
          if counter_map[key] == 1:
              return key