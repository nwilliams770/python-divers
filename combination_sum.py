class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfs(candidates, target, [], result)

        return result

    def dfs(self, candidates, target, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target-candidates[i], path+[candidates[i]], result)
