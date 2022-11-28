class Solution:
  def singleNumber(self, nums: List[int]) -> int:
      return reduce(lambda total, num: total ^ num, nums)