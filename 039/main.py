from typing import List

class Solution:

    # dfs
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        return self.dfs(candidates, target, 0)
        
    def dfs(self, candidates: List[int], target: int, candidate_index: int) -> List[List[int]]:
        result: List[List[int]] = []
        for i in range(candidate_index, len(candidates)):
            c = candidates[i]
            if c > target:
                continue
            if c == target:
                result.append([c])
                continue
            sub_results = self.dfs(candidates, target-c, i)
            for sub_result in sub_results:
                r = [c]
                r.extend(sub_result)
                result.append(r)
        return result

    # dp
    def combinationSumDP(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0 or target == 0:
            return []
        result: List[List[List[int]]] = [None] * (target + 1)
        result[0] = [[]]
        for c in candidates:
            for v in range(c, target+1):
                if result[v-c] is None:
                    continue
                for cs in result[v-c]:
                    if result[v] is None:
                        result[v] = []
                    cv = cs.copy()
                    cv.append(c)
                    result[v].append(cv)
        if result[target] is None:
            return []
        return result[target]
