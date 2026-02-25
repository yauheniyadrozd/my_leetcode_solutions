class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s=sorted(strs)
        first=s[0]
        last=s[-1]
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return first[:i]
        return first[:min(len(first),len(last))]