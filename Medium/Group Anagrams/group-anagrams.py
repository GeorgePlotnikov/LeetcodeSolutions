class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        data = defaultdict(list)
        
        for s in strs:
            data["".join(sorted(s))].append(s)
            
        return data.values()
